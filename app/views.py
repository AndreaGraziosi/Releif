from app import app
from flask import Flask, request, render_template, url_for 
import csv

#creatre a root... a decorator in parentheseis we put url we want to fire
#write a funcution underneath it and tell it to do something
# environment variables: run flask app... declare: $export FLASK_APP=run.py
# $export FLASK_ENV=development
#$flask run


my_yoga_pose = {
        'Menstrual Pain':'Paschimottanasana',
        'Low Back Pain':'Supta-Padangusthasana',
        'Eyes': 'Sarvangasana',
        'Flat Foot': 'Mulabandhasana',
        'Knees': 'Virasana',
        'Insomnia': 'Uttanasana'
    }

my_yoga_pictures = {
        'Menstrual Pain':'./static/img/Paschimotanasana.png',
        'Low Back Pain':'./static/img/SuptaP.png',
        'Eyes': './static/img/Sarvangasana.png',
        'Flat Foot': './static/img/Mulabandhasana.png',
        'Knees': './static/img/Virasana.png',
        'Insomnia': './static/img/uttanasana.jpg'

}    

my_yoga_sequences = {
    'Back-Bend':'./static/img/Backbends.png',
    'Forward-Bend': './static/img/ForwardBends.png',
    'Twist':'./static/img/twist.png',
    'Standing-Poses':'./static/img/StandingPoses.png',
    'Sitting-Poses':'./static/img/sittingPoses.png',
    'Inversions':'./static/img/Inversion.png'

}
sequence_poses = {
    'Back-Bend': ['./static/img/bb1.png','./static/img/bb2.png', './static/img/bb3.png'],
    'Forward-Bend':['./static/img/ff1.png', './static/img/ff2.png', './static/img/ff3.png'],
    'Twist':['./static/img/tw1.png','./static/img/tw2.png','./static/img/tw3.png'],
    'Standing-Poses':['./static/img/s1.png','./static/img/s2.png','./static/img/s3.png'],
    'Sitting-Poses':['./static/img/sp1.png', './static/img/sp2.png','./static/img/sp3.png'],
    'Inversions':['./static/img/i1.png','./static/img/i2.png','./static/img/i3.png']
}

@app.route("/")
def index():
    names = my_yoga_sequences
    return render_template("/index.html",  names=names)

@app.route("/sequence", methods=["GET", "POST"])
def sequence():
    pose = request.args.get("name")
    
    sequence = sequence_poses[pose] 
        
    context = {
    'sequence_category':my_yoga_sequences.keys(),
    'sequence_poses':sequence_poses

    }
    return render_template('/sequence.html', **context, sequence=sequence)


@app.route("/enter_problem", methods=['GET'])
def enter_problem():

    context = {
    'pose_names':my_yoga_pose.keys(),
    }
    return render_template("/enter_problem.html", **context)

@app.route("/display_pose", methods=['GET'])
def display_pose():
    
    chosen_ailment = request.args.get('pose')

    context = {
    'pose_names':my_yoga_pose.keys(),
    'pose_cure':my_yoga_pose.get(chosen_ailment, ""),
    'pose_image':my_yoga_pictures.get(chosen_ailment, "")
    }
    
    return render_template("/display_pose.html", **context, chosen_ailment=chosen_ailment)
    