from app import app
from models.Scheduling_model import Scheduling
from models.authentication_model import auth_model
from flask import jsonify, request

obj = Scheduling()

@app.route("/schedule")
def depart_Schedule_controller():
    return obj.depart_schedule()