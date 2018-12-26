# TODO: Implement modification/validation logic
# TODO: Default values
# TODO: Use datetime module for time handling
# TODO: KeyError for days and empty input
from utilities import parse_day, parse_time, parse_command, parse_command_num
from exceptions import *
from schedule import create_schedule
from backend import *


class User(db.Model):
    """"
    Generic User database class, ripped from the interwebs
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class Section(db.Model):
    """
    The Section class contains the time and days of a course section.
    It allows for the modification of a section's timeslot and scheduled days
    """
    __tablename__ = 'sections'
    id = db.Column(db.Integer, primary_key=True)
    section_id = db.Column(db.String(80), unique=False)
    time_start = db.Column(db.Integer, unique=False)
    time_end = db.Column(db.Integer, unique=False)
    Monday = db.Column(db.BOOLEAN, unique=False)
    Tuesday = db.Column(db.BOOLEAN, unique=False)
    Wednesday = db.Column(db.BOOLEAN, unique=False)
    Thursday = db.Column(db.BOOLEAN, unique=False)
    Friday = db.Column(db.BOOLEAN, unique=False)
    Saturday = db.Column(db.BOOLEAN, unique=False)
    Sunday = db.Column(db.BOOLEAN, unique=False)
    db_schedule = db.relationship("DBFinalSectionSelection", backref="backref_schedule", lazy=True)
    section_course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

    # CONSTRUCTOR
    def __init__(self, course, section_id, time_start=-1, time_end=-1, day="0"):
        self.course = course
        self.section_id = section_id
        self.time_start = time_start  # need to initialize this to save to table
        self.time_end = time_end  # this too
        self.timeslot = (time_start, time_end)
        self.day = day # this is just testing for database
        self.Monday = False
        self.Tuesday = False
        self.Wednesday = False
        self.Thursday = False
        self.Friday = False
        self.Saturday = False
        self.Sunday = False
        self.days = [0,0,0,0,0,0,0] # stores days at bits starting with Sunday
    # OPERATOR OVERLOADS
    def __str__(self):
        return f"Section ID: {self.section_id} Time: {self.timeslot} Days: {self.days}"  
    # INTERFACE
    def interface(self):
        while True:
            print("\n[SECTION MODIFICATION]")
            print(self)
            self.print_commands()
            try:
                user_res = parse_command_num(input("Enter a command via the command number: "), 5)
                # Validate input as a number 
                if user_res == 1:
                    self.set_timeslot()
                elif user_res == 2:
                    self.add_day()
                elif user_res == 3:
                    self.remove_day()
                elif user_res == 4:
                    self.remove_all_days()
                elif user_res == 5: # Exit interface for Section
                    break
            except ValueError:
                print("[ERROR] Invalid command. Please enter a number between 1 and 5")

    # COMMAND METHODS
    def set_timeslot(self):
        while True:
            try:
                time_start = parse_time(input("Please enter the START time of the section as minutes since 12AM: "))
                time_end = parse_time(input("Please enter the END time of the section as minutes since 12AM: "))
                if time_end < time_start:
                    raise EndBeforeStartTimeException
                self.timeslot = (time_start, time_end)
                break
            except ValueError:
                print("You provided an invalid input, please try again")
            except IndexError:
                print("The provided time is out of range, please try again")
            except EndBeforeStartTimeException:
                print("The provided end time is before the start time, please try again")
    def add_day(self):
        while True:
            try:
                user_day_res = parse_day(input("Please enter the day you want to add: "))
                self.days[user_day_res] = 1
                break
            except:
                print("You provided an invalid input, please try again.")
    def remove_day(self):
        while True:
            try:
                user_day_res = parse_day(input("Please enter the day you want to remove: "))
                self.days[user_day_res] = 0
                break
            except:
                print("You provided an invalid input, please try again.")
    def remove_all_days(self):
        self.days = [0,0,0,0,0,0,0]
        print("Removed all days for this section")

    # UTILITY METHODS
    @staticmethod 
    def print_commands():
        """
        Displays valid commands for the Section class 
        """
        print("1) Change timeslot")
        print("2) Add a day")
        print("3) Remove a day")
        print("4) Remove all days")
        print("5) Return to course interface")  


class Course(db.Model):
    """
    The Course class stores a dictionary of its sections.
    It is used to add, modify, and remove its contained sections 
    """
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(80), unique=False)
    course_name = db.Column(db.String(80), unique=False)
    db_sections = db.relationship("Section", backref="backref_course", lazy=True)

    # CONSTRUCTOR
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.sections = {}
        
    # COMMAND METHODs
    def add_section(self):        
        """
        Add section to Course
        Command Number: 1
        """
        section_id = input("Please enter the section ID: ")
        if self.section_exists(section_id):
            print(f"[ERROR] The following section already exists: {section_id}")
            return
        else:
            self.sections[section_id] = Section(self, section_id) # instantiate new section 
            
            self.sections[section_id].set_timeslot()
            # Loop to allow user to add multiple days at once
            while True:
                # TODO: Day and time validation
                # TODO: Allow user to input multiple days in one input string
                self.sections[section_id].add_day()
                user_res = input("Do you want to add another day for this section? (Y/N): ").upper()
                if user_res == "N":
                    break
                elif user_res != "Y":
                    print("[ERROR] Invalid command. Please try again") 

    def modify_section(self):
        """
        Brings user to section modification menu
        Command Number: 2
        """
        user_sel_section = input("Please enter the section ID you want to modify: ")
        if self.section_exists(user_sel_section):
            self.sections[user_sel_section].interface()
        else:
            print(f"The following section does not exist: {user_sel_section}")

    def remove_section(self):
        """
        Remove section from Course
        Command Number: 3
        """
        user_selected_course = input("Please enter the section ID you want to remove: ")
        if self.section_exists(user_selected_course):
            self.sections.pop(user_selected_course)
        else:
            print(f"The following section does not exist: {user_selected_course}")

    # INTERFACE
    def interface(self):
        while True:
            print("\n[COURSE MODIFICATION]")
            print(f"Course: {self.course_id} - {self.course_name}")
            self.print_sections() # show sections in current course
            self.print_commands()
            try:
                user_res = parse_command_num(input("Enter a command via the command number: "), 4)
                # Validate input as a number 
                if user_res == 1:
                    self.add_section()
                elif user_res == 2:
                    self.modify_section()
                elif user_res == 3:
                    self.remove_section()
                elif user_res == 4:
                    break
            except ValueError:
                print("[ERROR] Invalid command. Please enter a number between 1 and 3")

    # UTILITY METHODS
    def __repr__(self):
        print("Section ID: ", self.course_id, "\n")
        print("----------------------------------------")

    def __str__(self):
        return f"Course #: {self.course_id} Course Name: {self.course_name}"

    @staticmethod
    def print_commands():
        """
        Displays valid commands for the Course class 
        """
        print("1) Add a new section")
        print("2) Modify a section")
        print("3) Remove a section")
        print("4) Return to main menu")

    def print_sections(self):
        """
        Displays the sections contained by the Course class as a list
        """
        print(f"Number of Sections: {len(self.sections)}")
        print("-----------------------------------------------------")
        # Check if course list is empty
        if len(self.sections):
            counter = 1
            for section_id in self.sections:
                print(f"{counter} - {self.sections[section_id]}")
                counter += 1
        else:
            print("<<<You have added no sections to this course>>>")
        print("-----------------------------------------------------")

    def section_exists(self, section_id):
        return section_id in self.sections.keys()


class DBFinalSectionSelection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schedule_id = db.Column(db.Integer, unique=False)
    section_id = db.Column(db.Integer, db.ForeignKey('sections.id'), nullable=False)

    def __init__(self, schedule_id):
        self.schedule_id = schedule_id


class Database:
    """
    The Database class is pseudo-database of courses stored as a dictionary

    It is used to add, modify, and remove its contained courses 
    """
    def __init__(self):
        self.courses = {}

    # COMMAND METHODS
    def add_course(self):
        """
        Adds course to Database
        Command Number : 1
        """
        course_id = input("Please enter the course number: ") # asks user to input course num 
        course_name = input("Please enter the course name: ") # asks user to input course name
        if self.course_exists(course_id): # checks if the course number already exists
            print(f"[ERROR] The following course already exists: {course_id}")
        else: 
            self.courses[course_id] = Course(course_id, course_name) # instantiate new Course object
            print(f"Successfully added the following course: {course_name}")

    def modify_course(self,course_id):
        """
        Brings user to Course modification menu
        Command Number : 2
        """
        if self.course_exists(course_id):
            print(f"Selected the following course for modification: {course_id}")
            self.courses[course_id].interface() # Initialize command interface for course
        else:
            print(f"[ERROR] The provided course number does not exist: {course_id}")

    def remove_course(self, course_id):
        """
        Removes course from Database
        Command Number : 3
        """
        if self.course_exists(course_id):
            self.courses.pop(course_id) # remove course from database
            print(f"Successfully removed the following course: {course_id}")
        else:
            print("[ERROR] The provided course number does not exist:" + course_id)
    
    def gen_schedules(self):
        print("TYe")
        section_pools = [tuple(self.courses[course].sections.values()) for course in self.courses] 
        print("SECTION POOLS", section_pools)
        valid_schedules = create_schedule(section_pools)
        print("VALID SCHEDULES", valid_schedules)
        for schedule in valid_schedules:
            print(schedule)
    # INTERFACE METHOD
    def interface(self):
        while True:
            print("\n[MAIN MENU]") # prints newline for readability 
            self.print_courses() # show user added courses
            self.print_commands() # show user available commands
            try:
                user_res = parse_command_num(input("Enter a command via the command number: "), 4)
                # Validate input as a number 
                if user_res == 1:
                    self.add_course()
                elif user_res == 2:
                    user_selected_course = input("Please enter the course number you want to modify: ")
                    self.modify_course(user_selected_course)
                elif user_res == 3:
                    user_selected_course = input("Please enter the course number you want to remove: ")
                    self.remove_course(user_selected_course)
                elif user_res == 4:
                    self.gen_schedules()
            except ValueError:
                print("[ERROR] Invalid command. Please enter a number between 1 and 3")

    # UTILITY METHODS
    @staticmethod # function decorator for a static method (python's version of const) 
    def print_commands():
        """
        Displays valid commands for the Database class 
        """
        print("1) Add a new course")
        print("2) Modify a course")
        print("3) Remove a course")
        print("4) Generate Valid Schedules")

    def print_courses(self):
        """
        Displays the courses contained by the Database class as a list
        """
        print(f"Number of Courses: {len(self.courses)}")
        print("-----------------------------------------------------")
        # Check if course list is empty
        if len(self.courses):
            counter = 1
            for course_id in self.courses:
                print(f"{counter} - {self.courses[course_id]}")
                counter += 1
        else:
            print("<<<You have added no courses>>>")
        print("-----------------------------------------------------")

    def course_exists(self, course_id):
        return course_id in self.courses.keys()