from google.adk.agents import Agent
from .tools.weather_tool import get_weather
from .tools.time_tool import get_current_time

#agents instructions
agent_instructions = """
    Your a weather and time agent, you will provide weather updates and current time information.
"""

root_agent = Agent(
    name="weather_time_agent",
    model ="Gemini-2.0-flash",
    description="You are a weather and time agent. You will provide weather updates and current time information.",
    instructions = agent_instructions,
    tools= [get_weather, get_current_time],
)