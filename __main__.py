from agent.agent import Agent


def main():
    agent = Agent()
    print("Welcome to COBIE")
    print("Type 'exit'to quite.\n")
    print("Ask anything u want your COBIE to do ..:)")
    while True:
        user_input = input(">")

        if user_input.lower().strip() == "exit":
            print("Hope u like COBIE")
            break
        if not user_input.strip():
            continue

        response = agent.run(user_input)
        print("\nCOBIE ->")
        print(response)
        print()


if __name__ == "__main__":
    main()
