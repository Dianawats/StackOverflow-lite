from flask import Flask
from .config import app_config

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config["development"])

"""
This function helps to generater ids for
list items automatically
"""

id = 0


def generate_id(_list):
    
    if len(_list) == 0:
        id = len(_list) + 1
    else:
        id = id + 1
    return id

from api.views import auth
app.register_blueprint(auth)
from api.views.my_questions import my_questions
app.register_blueprint(my_questions)
