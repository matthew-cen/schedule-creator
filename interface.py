# TODO: Implement Exceptions

# IMPORTS
from classes import Database
# CONSTANTS
VALID_DAY_LST = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


# MAIN
def main():
    # initialize new database
    database = Database()

    # Initialize main user interface
    database.interface()

if __name__ == "__main__":
    main()