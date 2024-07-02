from app import app
from models.user_model import  user_model
from models.authentication_model import auth_model
from flask import jsonify, request

obj = user_model()
auth = auth_model()


@app.route("/teacher/getall")
@auth.token_auth()
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/teacher/addone",methods=["POST"])
@auth.token_auth()
def user_addone_controller():
    return obj.user_addone_model()

@app.route("/teacher/update",methods=["PUT"])
@auth.token_auth()
def user_update_controller():
    return obj.user_update_model()

@app.route("/teacher/delete/",methods=["DELETE"])
@auth.token_auth()
def user_delete_controller():
    return obj.user_delete_model()

@app.route("/teacher/patch/",methods=["PATCH"])
@auth.token_auth()
def user_patch_controller():
    return obj.user_patch_model()


@app.route("/teacher/getone/")
@auth.token_auth()
def user_getone_controller():
    return obj.user_getone_model()

@app.route("/teacher/login",methods=["POST"])
def teacher_login_controller():
    return  obj.teacher_login_model(request.form)

@app.route("/teacher/multiple",methods=["POST"])
@auth.token_auth()
def teacher_add_multiple_controller():
    return obj.teacher_add_multiple_model(request.json)

