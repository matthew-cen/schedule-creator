from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from classes import *
from flask import render_template, redirect, request, url_for
import pickle
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xawds12300@localhost/schedules'

db = SQLAlchemy(app)

app.debug = True

def clear_data(session):
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table %s' % table)
        session.execute(table.delete())
    session.commit()


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
    print("this is html_days", html_days)

    section.backref_course = this_course
    print(section)

    days = [0, 0, 0, 0, 0, 0, 0]
    for char in html_days:
        if char != ",":
            days[int(char)-1] = 1

    section.days = pickle.dumps(days) # uses pickle to convert into something that can be stored in database
    print("this is the after days", days)

    db.session.add(section)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/post_schedules', methods=["POST"])
def post_schedules():
    pass

if __name__ == "__main__":
    app.run()
    db.drop_all()
    db.create_all()