def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    if day_of_week == 1:
        return 'Sunday'
    if day_of_week == 2:
        return 'Monday'
    if day_of_week == 3:
        return 'Tuesday'
    if day_of_week == 4:
        return 'Wednesday'
    if day_of_week == 5:
        return 'Thursday'
    if day_of_week == 6:
        return 'Friday'
    if day_of_week == 7:
        return 'Saturday'
    else:
        return None

# SB Solution:
#     DAYS = [
#         "Sunday",
#         "Monday",
#         "Tuesday",
#         "Wednesday",
#         "Thursday",
#         "Friday",
#         "Saturday",
#     ]

#     if day_of_week < 1 or day_of_week > 7:
#         return None

#     return DAYS[day_of_week - 1]
