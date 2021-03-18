from app import app
from flask import Flask, request, render_template, url_for 
import csv

#creatre a root... a decorator in parentheseis we put url we want to fire
#write a funcution underneath it and tell it to do something
# environment variables: run flask app... declare: $export FLASK_APP=run.py
# $export FLASK_ENV=development
#$flask run
@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/enter_problem", methods=['GET'])
def enter_problem():
    return render_template("/enter_problem.html")

@app.route("/display_pose", methods=['POST'])
def display_pose():
    '''f = open("poses.csv", "r")
    reader = csv.reader(f)
    poses = list(reader)
    f.close()
    '''
    return render_template("/display_pose.html")

@app.route("/enter_poses", methods=['GET'])
def enter_poses():

    myData = {
    'name': request.args.get('name'),
    'ailment': request.args.get('ailment'),
    'special_instructions': request.args.get('special_instructions'),
    'pose_image': request.args.get('pose_image')
    }
    myFile = open("./poses.csv", "a")
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)
    myFile.close()
    return render_template("/enter_poses.html")

@app.route("/login")
def login():
    return render_template("/login.html")