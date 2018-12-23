# TODO: Implement modification/validation logic
# TODO: Generate schedule inferface
# TODO: Default values


class Section:
    timeslot = None
    def __init__(self, section_id):
        self.section_id = section_id
        self.timeslot = ()
        self.days = [0,0,0,0,0,0,0] # stores days at bits starting with Sunday
    def __str__(self):
        return f"Section ID: {self.section_id} Time: {self.timeslot} Days: {self.days}"  

    def interface(self):
        while True:
            print(self)
            self.print_commands()
            try:
                user_res = int(input("Enter a command via the command number: "))
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
                time_start = int(input("Please enter the START time of the section as minutes since 12AM: "))
                time_end = int(input("Please enter the END time of the section as minutes since 12AM: "))
                self.timeslot = (time_start, time_end)
            except:
                print("You provided an invalid input, please try again.")
    def add_day(self):
                user_day_res = parse_day(input("Please enter the day of the week the this section takes place: "))
                self.days[user_day_res] = 1
    # UTILITY METHODS
    @staticmethod 
    def print_commands():
        print("1) Change timeslot")
        print("2) Add a day")
        print("3) Remove a day")
        print("4) Remove all days")
        print("5) Return to course interface")  
class Course:
    # FIELDS
    sections = {}
    # METHODS
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        
    # COMMAND METHODs
    def add_section(self):        
        section_id = input("Please enter the section ID: ")
        if self.section_exists(section_id):
            print(f"[ERROR] The following section already exists: {section_id}")
            return
        else:
            self.sections[section_id] = Section(section_id) # instantiate new section 
            
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

    def modify_section(self, section_id):
        if self.section_exists(section_id):
            pass
        else:
            print(f"The following section does not exist: {section_id}")

    def remove_section(self, section_id):
        if self.section_exists(section_id):
            self.sections.pop(section_id)
        else:
            print(f"The following section does not exist: {section_id}")

    # INTERFACE
    def interface(self):
        while True:
            print(f"\nCourse: {self.course_id} - {self.course_name}")
            self.print_sections() # show sections in current course
            self.print_commands()
            try:
                user_res = int(input("Enter a command via the command number: "))
                # Validate input as a number 
                if user_res == 1:
                    self.add_section()
                elif user_res == 2:
                    user_selected_course = input("Please enter the course number you want to modify: ")
                    self.modify_section(user_selected_course)
                elif user_res == 3:
                    user_selected_course = input("Please enter the course number you want to remove: ")
                    self.remove_section(user_selected_course)
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
        print("1) Add a new section")
        print("2) Modify a section")
        print("3) Remove a section")
        print("4) Return to main menu")

    def print_sections(self):
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

class Database:
    """
    pseudo-database stored as dictionary
    """
    # FIELDS
    courses = {}

    # COMMAND METHODS
    def add_course(self):
        """
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
        Command Number : 2
        """
        if self.course_exists(course_id):
            print(f"Selected the following course for modification: {course_id}")
            self.courses[course_id].interface() # Initialize command interface for course
        else:
            print(f"[ERROR] The provided course number does not exist: {course_id}")

    def remove_course(self, course_id):
        """
        Command Number : 3
        """
        if self.course_exists(course_id):
            self.courses.pop(course_id) # remove course from database
            print(f"Successfully removed the following course: {course_id}")
        else:
            print("[ERROR] The provided course number does not exist:" + course_id)
    
    @staticmethod
    def gen_schedules(self):
        pass
        
    # INTERFACE METHOD
    def interface(self):
        while True:
            print() # prints newline for readability 
            self.print_courses() # show user added courses
            self.print_commands() # show user available commands
            try:
                user_res = int(input("Enter a command via the command number: "))
                # Validate input as a number 
                if user_res == 1:
                    self.add_course()
                elif user_res == 2:
                    user_selected_course = input("Please enter the course number you want to modify: ")
                    self.modify_course(user_selected_course)
                elif user_res == 3:
                    user_selected_course = input("Please enter the course number you want to remove: ")
                    self.remove_course(user_selected_course)
            except ValueError:
                print("[ERROR] Invalid command. Please enter a number between 1 and 3")

    # UTILITY METHODS
    @staticmethod # function decorator for a static method (python's version of const) 
    def print_commands():
        print("1) Add a new course")
        print("2) Modify a course")
        print("3) Remove a course")
        print("4) Generate Valid Schedules")

    def print_courses(self):
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