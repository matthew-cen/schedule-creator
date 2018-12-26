from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from classes import *
from flask import render_template, redirect, request, url_for
from schedule import create_schedule2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xawds12300@localhost/schedules'
db = SQLAlchemy(app)
app.debug = True

@app.route('/')
def index():
    return render_template("schedulecreatortest.html")

@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['username'], request.form['email'])
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('index'))

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


@app.route('/post_schedules', methods=["POST"])
def post_schedules():
    rows = db.session.query(Course).count()  # gets the number of rows
    before_product_sections = []
    for i in range(1, rows+1):
        curr_course = Course.query.filter_by(id=i).first()  # searches the course table by id
        before_product_sections.append(curr_course.db_sections) # adds the sections

    after_product_sections = create_schedule2(before_product_sections) # returns the possible schedule combinations as tuples in a list

    for schedule_id in range(1, len(after_product_sections)+1):  # starts from 1 because it will be stored as id
        for combinations in after_product_sections:  # loops through the possible combinations of sections
            for sections in combinations:  # iterates through each section individually
                new_db_section = DBFinalSectionSelection(schedule_id) # create a new schedule of sections class
                object_session = db.object_session(sections)  # since the section is already stored in session, need to reference it
                new_db_section.backref_schedule = sections  # set the the foreign key to the session
                object_session.add(new_db_section) # adds the new schedules of sections to the session of the section
                object_session.commit() # commit new object

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
    db.drop_all()
    db.create_all()