VALID_DAYS = {"SUNDAY" : 0, "MONDAY": 1, "TUESDAY": 2, "WEDNESDAY": 3, "THURSDAY": 4, "FRIDAY": 5, "SATURDAY": 6}
def parse_day(day_str):
    return VALID_DAYS[day_str.strip().upper()]

def parse_time(time_int): # parses time passed as integer as minutes since 00:00
    parsed_int = int(time_int)
    if parsed_int >= 0 and parsed_int < 1440:
        return parsed_int
    else:
        raise IndexError