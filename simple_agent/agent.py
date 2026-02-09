from google.adk.agents import Agent

#agents instructions
agent_instructions = """
    Your a greeting agent, you will greet the user and ask how you can help them. You will not do anything else, just greet the user and ask how you can help them.
"""

root_agent = Agent(
    name="greeting_agent",
    model ="Gemini-2.0-flash",
    description="You are a greeting agent. You will greet the user and ask how you can help them.",
    instructions = agent_instructions,
    tools= []
)