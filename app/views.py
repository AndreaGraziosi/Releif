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
    
    with open('poses.csv', newline='') as myFile:
        reader = csv.reader(myFile)
        for row in reader:
            print(row)
    myFile.close()
    
    return render_template("/display_pose.html")


my_yoga_pose = {
        'Menstrual Pain':'Supta-Virasana, Supta-Baddha-Konasana, Paschimottanasana',
        'Low Back Pain':'Supta-Padangusthasana, Adhomukha-Svanasana, Ustrasana',
        'Eyes': 'Sirsasana, Sarvangasana, Uttanasana',
        'Flat foot': 'Virasana, Mulabandhasana, Paschimotanasana',
        'knees': 'Gomukhasana, Virasana, Janu-Sirsasana',
        'Insomnia': 'Uttanasana, Paschimottanasana'
    }


@app.route("/enter_poses", methods=['GET'])
def enter_poses():
# This is to make sure the HTTP method is 
# POST and not any other
        '''if request.method == 'GET':
        name =  request.args.get('name')
        ailment = request.args.get('ailment')
        special_instructions = request.args.get('special_instructions')
        pose_image = request.args.get('pose_image')
        fieldnames = [name, ailment, special_instructions, pose_image]
        # TODO: enter name of your CSV file below
        with open('poses.csv','w') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow({'name': name, 'ailment': ailment, 'special_instructions':special_instructions, 'pose_image':pose_image})'''
    
        chosen_ailment = request.args.get('name')

        context = {
           'pose_names':my_yoga_pose.keys(),
           'pose_cure':my_yoga_pose.get(chosen_ailment, "")
        }

        return render_template("/enter_poses.html", **context)

@app.route("/login")
def login():
    return render_template("/login.html")