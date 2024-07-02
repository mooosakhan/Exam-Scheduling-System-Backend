from app import app
from models.classrooms_model import classrooms
from flask import request
from models.authentication_model import auth_model
from controller.user_controller import auth

obj = classrooms()

@app.route("/classrooms/getall")
@auth.token_auth()
def classrooms_getall_controller():
    return obj.classrooms_getall_model()

@app.route("/classrooms/addone",methods=["POST"])
@auth.token_auth()
def classrooms_addone_controller():
    return obj.classrooms_addone_model()

@app.route("/classrooms/patch",methods=["PATCH"])
@auth.token_auth()
def classrooms_patch_controller():
    return obj.classrooms_patch_model()

@app.route("/classrooms/delete",methods=["DELETE"])
@auth.token_auth()
def classrooms_delete_controller():
    return obj.classrooms_delete_model()