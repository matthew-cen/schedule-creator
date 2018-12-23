# TODO: Implement Exceptions

# IMPORTS
from datetime import *
# CONSTANTS
VALID_DAY_LST = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

# UTILITIES

# CLASSES
class Section:
    timeslots = []
    def __init__(self, section_id):
        self.section_id = section_id                                                            
    def add_time_slot(self, timeLow, timeHigh): # Chris add time slot 6:19pm
        timeslots.append((timeLow, timeHigh))

class Course:
    # FIELDS
    sections = []
    
    # METHODS
    def __init__(self, course_num, course_name):
        self.course_num = course_num
        self.course_name = course_name
    # def add_section

    def add_section(self, section): # Chris add section 6:19
        # i don't think i'm adding the section thing correctly... (we gotta declare type)? 
        self.sections.append(section) 
    # def add_timeslot

    def __repr__(self):
        print("Course Name: ", self.course_name, "\n")
        print("Course Number: ", self.course_num, "\n")
        print("----------------------------------------")

class Database:
    """
    pseudo-database stored as dictionary

    """
    # FIELDS
    courses = {}
    # METHODS
    def add_course(self):
        course_num = input("Please enter the course number: ") # asks user to input course num 
        course_name = input("Please enter the course name: ") # asks user to input course name
        self.courses[course_num] = Course(course_num, course_name) # instantiate new Course object
    
    def modify_course(self,course_num):
        pass
    def print_courses(self):
        print("Number of Courses: ", end="")
        # Check if course list is empty
        if len(self.courses):
            print(len(self.courses))
            counter = 1
            for course in self.courses:
                print(counter + ")" + self.courses[course])
        else:
            print("0 \nYou have added no courses")
    def remove_course(self, course_num):
        try:
            courses.pop(course_num) # remove course from database
        except KeyError:
            print("[ERROR] The provided course number does not exist:" + course_num)
    def interface(self):
        self.print_commands() # show user available commands
        while true:
            user_res = input("Enter a command via the command number: ")
            
            # Validate input as a number 
            if user_res == 1:
                self.add_course()
            elif user_res == 2:
                self.modify_course()
            elif user_res == 3:
                self.remove_course()
            else:
                print("Invalid command. Please enter a number between 1 and 3")


    @staticmethod # function decorator for a static method (python's version of const) 
    def print_commands(self):
        print("1) Add a new course")
        print("2) Modify a course")
        print("3) Remove a course")


# MAIN
def main():
    # initialize new database
    database = Database()

    # Output current courses
    database.print_courses()

    
    # Main User Interface Loop
    while True: # true and false need to capitalize first letter
        print("0 - Monday, 1 - Tuesday, 2 - Wednesday, 3 - Thursday, 4 - Friday, 5 - Saturday, 6 - Sunday")
    
        res_day = input("Please select a day using the number or the day name : ")
        if res_day.lower() not in VALID_DAY_LST or res_day.isdigit(): 
            # if the input was invalid            
            print("Invalid input, please try again - You provided: ", res_day)
        else: 
            # if the input was valid                                                           
            while True:
                res_timeslot = input("Please enter the start and end times for timeslot in 24HR format (ex. 03:30) :")
                # input format is like "0600 2300" initially (beta version)                                
                # res_timeslot is string input
                # have to exit from while loop, no break (next line code unreachable on pycharm)
                if (0 < int(res_timeslot[0:3]) < 2400 and 0 < int(res_timeslot[5:8]) <2400):
                    newClass = Course(course_name, course_num)
                    # checks if number is between 0 and 2400
                    # need to store the time slot into something
                    break                
            if not input("Add more timeslots? (Y/N):"):
                break
            if not input("Add more days?"):
                res_repeat = input("Do you want to copy over existing timeslots from previous days? (Y/N): ")
            if
            break

main()