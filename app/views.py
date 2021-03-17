from app import app
from flask import Flask, request, render_template 

#creatre a root... a decorator in parentheseis we put url we want to fire
#write a funcution underneath it and tell it to do something
# environment variables: run flask app... declare: $export FLASK_APP=run.py
# $export FLASK_ENV=development
#$flask run
@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/enter_problem", methods=['POST'])
def enter_problem():
    ailment = request.form.get("name")
    if not ailment:
        return "Please enter an ailment"
    return render_template("/display_pose.html")

@app.route("/display_pose", methods=['POST'])
def display_pose():
   
    #capture value entered in enter problem
    # retrieve from the database
    return render_template("/display_pose.html")

