from functools import wraps
import _mysql_connector
import mysql.connector
import jwt
import json
from flask import request
from flask import make_response
import re


class auth_model():
    #connectionn stablishment code
    def __init__(self):
        try:
             self.con = mysql.connector.connect(host="localhost",username="root",password="caamodel@1",database="mydatabase")
             self.con.autocommit=True
             self.cur=self.con.cursor(dictionary=True)
             print("CONNECTION SUCCESSFULL")
        except:
            print("some error")

    def token_auth(self,endpoint=""):
        def inner1(func):
            @wraps(func)
            def inner2(*args):
                endpoint = request.url_rule
                authorzation = request.headers.get("Authorization")
                if re.match("^Bearer *([^ ]+) *$", authorzation, flags= 0):
                    token = authorzation.split(" ")[1]
                    jwtdecoded = jwt.decode(token,"shirp123",algorithms="HS256")
                    role_id = jwtdecoded['payload']['Role_id']
                    self.cur.execute(f"SELECT roles FROM accessibilty_view WHERE endpoint = '{endpoint}'")
                    result = self.cur.fetchall()
                    if len(result)>0:
                        allowed_roles = json.loads(result[0]['Roles'])
                        if role_id in allowed_roles:
                            return func(*args)
                        else:
                            return make_response({"ERROR":"INVALID ROLE"},400)
                    else:
                        return make_response({"ERROR":"UNKOWN ERROR"},404)    
                else:
                    make_response({"ERROR":"INVALID TOKEN"},401)  

            return inner2
        return inner1
    