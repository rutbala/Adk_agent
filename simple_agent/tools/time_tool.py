import datetime
from zoneinfo import ZoneInfo

def get_current_time(city:str):
    """
    This tool is used to get the current time in a specific city. 

    Args:
        city: thhe name of the city you want to get the current time for.

    Returns:
        The current time in the specified city.
    """

    # Get the current time in the specified city
    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}