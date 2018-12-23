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

    # # Main User Interface Loop
    # while True: # true and false need to capitalize first letter
    #     print("0 - Monday, 1 - Tuesday, 2 - Wednesday, 3 - Thursday, 4 - Friday, 5 - Saturday, 6 - Sunday")
    
    #     res_day = input("Please select a day using the number or the day name : ")
    #     if res_day.lower() not in VALID_DAY_LST or res_day.isdigit(): 
    #         # if the input was invalid            
    #         print("Invalid input, please try again - You provided: ", res_day)
    #     else: 
    #         # if the input was valid                                                           
    #         while True:
    #             res_timeslot = input("Please enter the start and end times for timeslot in 24HR format (ex. 03:30) :")
    #             # input format is like "0600 2300" initially (beta version)                                
    #             # res_timeslot is string input
    #             # have to exit from while loop, no break (next line code unreachable on pycharm)
    #             if (0 < int(res_timeslot[0:3]) < 2400 and 0 < int(res_timeslot[5:8]) <2400):
    #                 newClass = Course(course_name, course_num)
    #                 # checks if number is between 0 and 2400
    #                 # need to store the time slot into something
    #                 break                
    #         if not input("Add more timeslots? (Y/N):"):
    #             break
    #         if not input("Add more days?"):
    #             res_repeat = input("Do you want to copy over existing timeslots from previous days? (Y/N): ")
    #         break

main()