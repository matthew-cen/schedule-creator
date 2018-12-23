VALID_DAYS = {"SUNDAY" : 0, "MONDAY": 1, "TUESDAY": 2, "WEDNESDAY": 3, "THURSDAY": 4, "FRIDAY": 5, "SATURDAY": 6}
def parse_day(day_str):
    return VALID_DAYS[day_str.upper]