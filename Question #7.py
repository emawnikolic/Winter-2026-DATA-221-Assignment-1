# Question 7 | Time Conversion Function -  Write a function that converts a given number of seconds since midnight into:
    # • Hours
    # • Minutes
    # • Seconds
    # • AM or PM
# The function should return a formatted string. If the input is invalid, return an appropriate message.

def seconds_conversion(seconds):
    if not isinstance(seconds, int):
        return "Input must be an integer."
    if seconds < 0 or seconds >= 86400:
        return "Seconds must be between 0 and 86400."

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds %= 60

    period = "AM" if hours < 12 else "PM"

    display_hour = hours % 12
    display_minute = minutes % 60
    display_second = seconds % 60

    if display_hour == 0:
        display_hour = 12

    return f"{display_hour:02d} {display_minute:02d} {seconds:02d} {period}"

print(seconds_conversion(38278))

