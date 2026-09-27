from agent.agent import Agent
from cli.commands import clear_history,show_help
from cli.ui import(show_goodbye,show_message,show_response,user_prompt,welcome)


def run_cli():
    agent = Agent()
    welcome()
    while True:
        user_input = user_prompt()
        if not user_input.strip():
            continue
        command = user_input.strip().lower()
        if command in ("/help", "help"):
            show_help()
            continue

        if command in ("/clear", "clear"):
            clear_history(agent)
            continue

        if command in ("/exit", "exit"):
            show_goodbye()
            break
        try:
            show_message("COBIE is thinkingg....")
            response = agent.run(user_input)
            show_response(response)
            
        except Exception as e:
            show_message(f"Error:{e}")


