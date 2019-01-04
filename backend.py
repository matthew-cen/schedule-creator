# TODO: Move security information separately
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from classes import *
from flask import render_template, redirect, request, url_for, jsonify
from schedule import create_schedule2
from flask_restplus import Resource, Api

# CONFIGURATION
app = Flask(__name__,
static_folder="./dist")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xawds12300@localhost/schedules'
app.debug = True

# INITIALIZATION
db = SQLAlchemy(app)

# API
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint)
app.register_blueprint(blueprint)

# TEST API ROUTE
@api.route("/hello")
class hello(Resource):
    def get(self):
        return "Hello"

# ROUTES
"""
Home root directory
"""
@app.route('/')
def index():
    return render_template("courseList.html")
    # return render_template("schedulefortest.html") temporarily commented out for web design testing 

@app.route('/delete_course', methods=['DELETE'])
def delete_course():
    delete_course_primary_id = request.form['delete_course_primary_id']
    delete = Course.query.filter_by(id=delete_course_primary_id).first()

    # don't know if we need to individually delete sections
    for sections in delete.db_sections:
        section_session = db.object_session(sections) # finds the sessions where the section is stored
        section_session.delete(sections)
        section_session.commit()


    course_session = db.object_session(delete) # finds the session where the course is stored
    course_session.delete(delete) # deletes the course
    course_session.commit()

    return redirect(url_for('index'))

@app.route('/delete_section', methods=['DELETE'])
def delete_section():
    delete_course_primary_id = request.form['delete_course_primary_id']
    delete_course_object = Course.query.filter_by(id=delete_course_primary_id).first()

    delete_section_id = request.form['delete_section_primary_id']

    for sections in delete_course_object.db_sections:
        if sections.section_id == delete_section_id: # if the sections in the courses is equal to the section id requested
            section_session = db.object_session(sections)
            section_session.delete(sections)
            section_session.commit()
            break

    return redirect(url_for('index'))


@app.route('/get_courses', methods=['GET'])
def get_courses():
    courses_dict = {}
    primary_key = request.form['primary_key']
    courses = Course.query.filter_by(id=primary_key)
    for course in courses:
        courses_dict[course.id] = course # returning a course class, dunno what it'll do

    return jsonify(courses_dict)

@app.route('/get_sections', methods=['GET'])
def get_sessions():
    sections_dict = {}
    primary_key = request.form['primary_key']
    sections = Section.query.filter_by(id=primary_key)
    for sections in sections:
        sections_dict[sections.id] = sections # returning a section class, dunno what it'll do

    return jsonify(sections_dict)

@app.route('/get_schedules', methods=['GET'])
def get_schedules():
    schedules_dict = {}
    primary_key = request.form['primary_key']
    schedules = DBFinalSectionSelection.query.filter_by(id=primary_key)
    for schedule in schedules:
        schedules_dict[schedule.id] = schedule # returning a schedule class, dunno what it'll do

    return jsonify(schedules_dict)

@app.route('/put_course', methods=['PUT'])
def put_course():
    course_primary_id = request.form['course_primary_id']
    new_course_name = request.form['new_course_name']
    new_course_id = request.form['new_course_id']

    course_object = Course.query.filter_by(id=course_primary_id).first()

    course_object.course_name = new_course_name
    course_object.course_id = new_course_id
    db.session.commit()


@app.route('/put_section', methods=['PUT'])
def put_section():
    section_primary_id = request.form['section_primary_id']
    new_section_name = request.form['new_section_name']
    new_section_id = request.form['new_section_id']
    new_time_start = request.form['new_time_start']
    new_time_end = request.form['new_time_end']
    monday = request.form['monday']
    tuesday = request.form['tuesday']
    wednesday = request.form['wednesday']
    thursday = request.form['thursday']
    friday = request.form['friday']
    saturday = request.form['saturday']
    sunday = request.form['sunday']

    section_object = Section.query.filter_by(id=section_primary_id)

    section_object.section_name = new_section_name
    section_object.section_id = new_section_id
    section_object.time_start = new_time_start
    section_object.time_end = new_time_end
    section_object.Monday = monday
    section_object.Tuesday = tuesday
    section_object.Wednesday = wednesday
    section_object.Thursday = thursday
    section_object.Friday = friday
    section_object.Saturday = saturday
    section_object.Sunday = sunday

    db.session.commit()


"""
Route for user login POST request 
"""
@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['username'], request.form['email'])
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('index'))

"""
Route for course creation POST request 
"""
@app.route('/post_course', methods=["POST"])
def post_course():
    this_course = Course(request.form['course_id'], request.form['course_name'])
    db.session.add(this_course)
    db.session.commit()

    return redirect(url_for('index'))

@app.route("/post_section", methods=["POST"])
def post_sections():
    # assumes that the courses are all unique
    course_name = request.form["course_id"]
    course_object = Course.query.filter_by(course_name=course_name).first()

    course_object_session = db.object_session(course_object)
    section = Section(course=course_object, section_id=request.form['section_id'], time_start=request.form['time_start'],
                      time_end=request.form['time_end'])
    html_days = request.form['day']
    # days is inputted as 1,3 (Monday, Wednesday)
    section.backref_course = course_object

    for char in html_days:
        if char != ",":
            if int(char) == 1:
                section.Monday = True
            if int(char) == 2:
                section.Tuesday = True
            if int(char) == 3:
                section.Wednesday = True
            if int(char) == 4:
                section.Thursday = True
            if int(char) == 5:
                section.Friday = True
            if int(char) == 6:
                section.Saturday = True
            if int(char) == 7:
                section.Sunday = True

    course_object_session.add(section)
    course_object_session.commit()

"""
Route for schedule generation POST request 
"""
@app.route('/post_schedules', methods=["POST"])
def post_schedules():
    if (db.session.query(DBFinalSectionSelection).count() != 0):
        last_id = db.session.query(DBFinalSectionSelection).order_by(DBFinalSectionSelection.id.desc()).first().schedule_id + 1
    else:
        last_id = 1
    rows = db.session.query(Course).count()  # gets the number of rows
    before_product_sections = []
    for i in range(1, rows+1):
        curr_course = Course.query.filter_by(id=i).first()  # searches the course table by id
        before_product_sections.append(curr_course.db_sections) # adds the sections

    after_product_sections = create_schedule2(before_product_sections) # returns the possible schedule combinations as tuples in a list

    for combinations in after_product_sections:  # loops through the possible combinations of sections
        for sections in combinations:  # iterates through each section individually
            new_db_section = DBFinalSectionSelection(last_id) # create a new schedule of sections class
            # https://stackoverflow.com/questions/24291933/sqlalchemy-object-already-attached-to-session
            object_session = db.object_session(sections)  # since the section is already stored in session, need to reference it
            new_db_section.backref_schedule = sections  # set the the foreign key to the session
            object_session.add(new_db_section) # adds the new schedules of sections to the session of the section
            object_session.commit() # commit new object
            last_id += 1 # increments the last id, so the next schedule will have new schedule_id

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
    db.drop_all()
    db.create_all()