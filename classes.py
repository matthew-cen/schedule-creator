class Section:
    timeslot = ()
    days = ()
    def __init__(self, section_id):
        self.section_id = section_id                                                            
    def add_time_slot(self, timeLow, timeHigh): 
        self.timeslot.extend((timeLow, timeHigh))

class Course:
    # FIELDS
    sections = {}
    
    # METHODS
    def __init__(self, course_num, course_name):
        self.course_num = course_num
        self.course_name = course_name
    # COMMAND METHODs
    def add_section(self):        
        # self.sections.append(section) 
        pass
    def modify_section(self, section_id):
        pass
    def remove_section(self, section_id):
        pass
    # INTERFACE
    def interface(self):
        while True:
            self.print_sections(self) # show sections in current course
            self.print_commands(self)

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
        print("Section ID: ", self.course_num, "\n")
        print("----------------------------------------")
    def __str__(self):
        return f"Course #: {self.course_num} Course Name: {self.course_name}"
    @staticmethod
    def print_commands(self):
        print("1) Add a new section")
        print("2) Modify a section")
        print("3) Remove a section")
        print("4) Return to main menu")

    @staticmethod
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
    @staticmethod
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
        course_num = input("Please enter the course number: ") # asks user to input course num 
        course_name = input("Please enter the course name: ") # asks user to input course name
        if course_num in self.courses.keys(): # checks if the course number already exists
            print(f"There is already a course with this course number with name: {self.courses[course_num]}")
        else: 
            self.courses[course_num] = Course(course_num, course_name) # instantiate new Course object
            print(f"Successfully added the following course: {course_name}")
    def modify_course(self,course_num):
        """
        Command Number : 2
        """
        print(f"Selected the following course for modification: {course_num}")
        pass

    def remove_course(self, course_num):
        """
        Command Number : 3
        """
        try:
            self.courses.pop(course_num) # remove course from database
            print(f"Successfully removed the following course: {course_num}")
        except KeyError:
            print("[ERROR] The provided course number does not exist:" + course_num)
    
    @staticmethod
    def gen_schedules(self):
        pass
    # INTERFACE METHOD
    def interface(self):
        while True:
            print() # prints newline for readability 
            self.print_courses(self) # show user added courses
            self.print_commands(self) # show user available commands
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
    def print_commands(self):
        print("1) Add a new course")
        print("2) Modify a course")
        print("3) Remove a course")
        print("4) Generate Valid Schedules")
    @staticmethod
    def print_courses(self):
        print(f"Number of Courses: {len(self.courses)}")
        print("-----------------------------------------------------")
        # Check if course list is empty
        if len(self.courses):
            counter = 1
            for course_num in self.courses:
                print(f"{counter} - {self.courses[course_num]}")
                counter += 1
        else:
            print("<<<You have added no courses>>>")
        print("-----------------------------------------------------")

    @staticmethod
    def course_exists(self, course_num):
        return course_num in self.courses.keys()