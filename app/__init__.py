from flask import Flask

app = Flask(__name__)


#importing the views file to avoid a circular import
from app import views
