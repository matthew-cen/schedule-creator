# TODO: Move security information separately
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from classes import *
from flask import render_template, redirect, request, url_for, jsonify
from schedule import create_schedule2

# CONFIGURATION
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xawds12300@localhost/schedules'
app.debug = True

# INITIALIZATION
db = SQLAlchemy(app)

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
    delete_course_name = request.form['delete_course_name']
    delete = Course.query.filter_by(course_name=delete_course_name).first()
    delete_id = delete.id

    db.session.delete(delete)

    course_sections = Section.query.filter_by(section_course_id=delete_id)
    for sections in course_sections:
        db.session.delete(sections)

    db.session.commit()

    return redirect(url_for('index'))

@app.route('/delete_course_id', methods=['DELETE'])
def delete_course_id():
    delete_course_id = request.form['delete_course_id']
    delete = Course.query.filger_by(course_id=delete_course_id)

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

    section = Section(course=this_course, section_id=request.form['section_id'], time_start=request.form['time_start'],
                      time_end=request.form['time_end'])
    html_days = request.form['day']

    section.backref_course = this_course

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

    db.session.add(section)
    db.session.commit()

    return redirect(url_for('index'))


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