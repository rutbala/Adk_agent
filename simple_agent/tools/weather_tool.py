def get_weather(city:str):
    """
    This tool is used to get the current weather in a specific city.

    Args:
        city: the name of the city you want to get the weather for.

    Returns:
        The current weather in the specified city.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                "Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for {city} is not available.",
        }