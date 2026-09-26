import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from tools.registry import ToolRegister

load_dotenv()


class Agent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        self.registry = ToolRegister()

        self.model = "gpt-5.6-luna"

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

Use tools when you need information about the user's project.

Do not pretend you used a tool when you did not.

Give clear and concise answers.
"""
        self.tools = [
            {
                "type": "function",
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
                    "additionalProperties": False,
                },
                "strict": True,
            },
            {
                "type": "function",
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
                    "additionalProperties": False,
                },
                "strict": True,
            },
            {
                "type": "function",
                "name": "list_directory",
                "description": "List files and directories inside a directory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Directory path."}
                    },
                    "required": ["path"],
                    "additionalProperties": False,
                },
                "strict": True,
            },
            {
                "type": "function",
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
                    "additionalProperties": False,
                },
                "strict": True,
            },
            {
                "type": "function",
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
                    "additionalProperties": False,
                },
                "strict": True,
            },
            {
                "type": "function",
                "name": "git_status",
                "description": "Show the current git status.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "additionalProperties": False,
                },
                "strict": True,
            },
            {
                "type": "function",
                "name": "git_diff",
                "description": "Show the current git diff.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "additionalProperties": False,
                },
                "strict": True,
            },
            {
                "type": "function",
                "name": "edit_file",
                "description": "Replace a specific piece of text in a file.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Path to the file."},
                        "old_text": {
                            "type": "string",
                            "description": "Existing text to replace.",
                        },
                        "new_text": {"type": "string", "description": "New text."},
                    },
                    "required": ["path", "old_text", "new_text"],
                    "additionalProperties": False,
                },
                "strict": True,
            },
        ]

    def run(self, user_message):
        response = self.client.responses.create(
            model=self.model,
            instructions=self.instructions,
            input=user_message,
            tools=self.tools,
        )

        while True:
            tool_calls = [
                item for item in response.output if item.type == "function_call"
            ]
            if not tool_calls:
                return response.output_text
            tool_outputs = []
            for tool_call in tool_calls:
                tool_name = tool_call.name
                arguments = json.loads(tool_call.arguments)
                result = self.registry.execute(tool_name, arguments)
                tool_outputs.append(
                    {
                        "type": "function_call_output",
                        "call_id": tool_call.call_id,
                        "output": json.dumps(result),
                    }
                )
            response = self.client.responses.create(
                model=self.model,
                instructions=self.instructions,
                previous_response_id=response.id,
                input=tool_outputs,
                tools=self.tools,
            )
