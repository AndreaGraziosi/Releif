from app import app
from flask import render_template

#creatre a root... a decorator in parentheseis we put url we want to fire
#write a funcution underneath it and tell it to do something
# environment variables: run flask app... declare: $export FLASK_APP=app.py
# $export FLASK_ENV=development
#$flask run
@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/enter_problem")
def enter_problem():
    return render_template("/enter_problem.html")

