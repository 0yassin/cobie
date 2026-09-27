import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from tools.registry import ToolRegister

load_dotenv()


class Agent:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.registry = ToolRegister()
        self.contents = []
        self.model = "gemini-3-flash-preview"
        self.instructions = """
You are COBIE, a local AI coding agent.

You help the user understand and work with their project.

You have access to tools that can:

- read files
- write files
- list directories
- search files
- run terminal commands
- inspect git status
- inspect git diff
- edit files

IMPORTANT RULES:

1. Do NOT use tools for normal conversation.
2. Do NOT use tools just because the user says something personal or conversational.
3. Only use a tool when the user's request actually requires information or an action involving the project.
4. If the user says something like " who am i whats my name", simply respond naturally and do not use any tool.
5. Remember information from the current conversation when answering later questions.
6. Do not pretend you used a tool when you did not.
7. Give clear and concise answers.
"""

        self.tools = [
            {
                "name": "read_file",
                "description": "Read and return the contents of a file.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Path to the file to read.",
                        }
                    },
                    "required": ["path"],
                },
            },
            {
                "name": "write_file",
                "description": "Write content to a file.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Path of the file to write.",
                        },
                        "content": {
                            "type": "string",
                            "description": "Content to write to the file.",
                        },
                    },
                    "required": ["path", "content"],
                },
            },
            {
                "name": "list_directory",
                "description": "List files and directories inside a directory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Directory path.",
                        }
                    },
                    "required": ["path"],
                },
            },
            {
                "name": "search_file",
                "description": "Search project files for a text query.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Text to search for.",
                        },
                        "path": {
                            "type": "string",
                            "description": "Directory to search in.",
                        },
                    },
                    "required": ["query", "path"],
                },
            },
            {
                "name": "run_command",
                "description": "Run a terminal command.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "command": {
                            "type": "string",
                            "description": "Terminal command to execute.",
                        }
                    },
                    "required": ["command"],
                },
            },
            {
                "name": "git_status",
                "description": "Show the current git status.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                },
            },
            {
                "name": "git_diff",
                "description": "Show the current git diff.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                },
            },
            {
                "name": "edit_file",
                "description": "Replace a specific piece of text in a file.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Path to the file.",
                        },
                        "old_text": {
                            "type": "string",
                            "description": "Existing text to replace.",
                        },
                        "new_text": {
                            "type": "string",
                            "description": "New text.",
                        },
                    },
                    "required": ["path", "old_text", "new_text"],
                },
            },
        ]

        self.config = types.GenerateContentConfig(
            system_instruction=self.instructions,
            tools=[types.Tool(function_declarations=self.tools)],
        )


    def run(self, user_message):
        self.contents.append(
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=user_message)
                ],
            )
        )

        while True:
            response = self.client.models.generate_content(
                model=self.model,
                contents=self.contents,
                config=self.config,
            )

            function_calls = response.function_calls

            if not function_calls:
                self.contents.append(response.candidates[0].content)
                return response.text

            self.contents.append(response.candidates[0].content)

            function_responses = []

            for function_call in function_calls:
                tool_name = function_call.name
                arguments = dict(function_call.args)

                print(f"[Tool] {tool_name}({arguments})")

                result = self.registry.execute(
                    tool_name,
                    arguments
                )

                function_responses.append(
                    types.Part.from_function_response(
                        name=tool_name,
                        response={
                            "result": result
                        },
                    )
                )

            self.contents.append(
                types.Content(
                    role="user",
                    parts=function_responses,
                )
            )
