VALID_DAYS = {"SUNDAY" : 0, "MONDAY": 1, "TUESDAY": 2, "WEDNESDAY": 3, "THURSDAY": 4, "FRIDAY": 5, "SATURDAY": 6}
def parse_day(day_str):
    return VALID_DAYS[day_str.strip().upper()]

def parse_time(time_int): # parses time passed as integer as minutes since 00:00
    parsed_int = int(time_int)
    if parsed_int >= 0 and parsed_int < 1440:
        return parsed_int
    else:
        raise IndexError
# Peforms command validation for commands of alphanumeric commands.
def parse_command(command_str, valid_comms):
    """
    valid_comms: Collection of valid commands
    """
    command_str = command_str.strip()
    if command_str in valid_comms:
            return command_str
    else:
        raise ValueError