from agent.agent import Agent

agent =Agent()
response = agent.run(
    "list the file in the current project and tell me what you find"
)
print("\n COBIE")
print(response)