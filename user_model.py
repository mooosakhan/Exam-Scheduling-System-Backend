import _mysql_connector
import mysql.connector
from datetime import datetime, timedelta
import jwt
import json
from flask import jsonify, make_response,request
class user_model():
    #connectionn stablishment code
    def __init__(self):
        try:
             self.con = mysql.connector.connect(host="localhost",username="root",password="caamodel@1",database="mydatabase")
             self.con.autocommit=True
             self.cur=self.con.cursor(dictionary=True)
             print("CONNECTION SUCCESSFULL")
        except:
            print("some error")
    
    def user_getall_model(self):
        #query execution code
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        print(result)
        if len(result)>0:
            return make_response({"payload" : result},200)
        else:
            return make_response({"MESSAGE ":"NO DATA FIND"},204)
        
    def user_getone_model(self):
        data = request.json
        if not data or  'id' not in data:
            return jsonify({"error": "Missing 'id' in request body"}), 400
        id = data.pop('id')
     
        try:    
            self.cur.execute(f"SELECT * FROM users WHERE id='{id}';")
            one_result = self.cur.fetchall()
            if not one_result:
             return make_response({"message": "No teacher found with the given ID"}, 404)
        
            return make_response({"RECQUIRED TEACHER " : one_result},201)
        except Exception as e:
            print(f"AN ERROR OCCURRED: {e}")

        
    def user_addone_model(self):
        data = request.json
        user_id = data.get('id')
        

        self.cur.execute("SELECT id FROM users")
        result = self.cur.fetchall()
        
        
        existing_ids = {row['id'] for row in result} 
        
        if user_id in existing_ids:
            return make_response({"message": "Teacher with this ID already exists"}, 200)
        else:
        #query execution code
            try:
                self.cur.execute(f"INSERT INTO users(id, department, name, freehourstoday,Role_id,email,password) VALUES('{data['id']}', '{data['department']}', '{data['name']}', '{data['freehourstoday']}',{data['Role_id']}, '{data['email']}', '{data['password']}')")
                return make_response({"message" : "ADDED SUCCESFULLY"},200)
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                return make_response({"message": "Duplicate Entry"}, 500)
            
    def user_update_model(self):
        data = request.json
        entered_id = data.get('id')
        update_query = """
            UPDATE users 
            SET department=%s, name=%s, freehourstoday=%s, Role_id=%s, email=%s, password=%s 
            WHERE id = %s
        """
        update_values = (data['department'], data['name'], data['freehourstoday'], data['Role_id'], data['email'], data['password'], entered_id)
        self.cur.execute(update_query, update_values)
        if self.cur.rowcount>0:
            return make_response({"message" : "User Updated successfully"},201)
        else:
            return make_response({"message" : "NOTHING TO UPDATE"},202)  
        
    def user_delete_model(self):
        data = request.json
        if not data or  'id' not in data:
            print(data)
            return jsonify({"error": "Missing 'id' in request body"}), 400
        id = data.pop('id')

        #query execution code
        self.cur.execute(f"DELETE FROM users WHERE id={id}")    
        if self.cur.rowcount>0:
            return make_response({"message" : "USER DELETED SUCCESSFULLY"},200)
        else:
            return make_response({"nessage" : "NOTHING TO DELETE"},202)
        
    def user_patch_model(self):
        data = request.json
        if not data or  'id' not in data:
            print(data)
            return jsonify({"error": "Missing 'id' in request body"}), 400
        id = data.pop('id')

        qry = "UPDATE users SET "
        for key in data:
            qry = qry + f"{key} = '{data[key]}',"
        
        qry = qry[:-1] + f" WHERE id={id}"
        self.cur.execute(qry)

        if self.cur.rowcount>0:
            return("Specific couloumn of the table has been updated")
        else:
            return("ERROR")  

    def teacher_login_model(self,data):
        self.cur.execute(f"SELECT id, department, name, freehourstoday, Role_id,email FROM users WHERE email='{data['email']}' and password='{data['password']}'")
        rezult = self.cur.fetchall()
        userdata = rezult[0]
        exp_time = datetime.now() + timedelta(minutes=1500)
        exp_epoch_time = int(exp_time.timestamp())
        payload = {
            "payload":userdata,
            "exp":exp_epoch_time
        }
        jwtoken =  jwt.encode(payload, "shirp123", algorithm="HS256")
        return make_response({"token":jwtoken},200)
    
    def teacher_add_multiple_model(self,data):
        qry = "INSERT INTO users(id, department, name, freehourstoday,Role_id,email,password) VALUES "
        for userdata in data:
            qry += f"( {userdata['id']},'{userdata['department']}','{userdata['name']}',{userdata['freehourstoday']} ,{userdata['Role_id']} ,'{userdata['email']}','{userdata['password']}'),"
        finalqry = qry.rstrip(",")
        self.cur.execute(finalqry)
        return make_response({"message" : "MILTIPLE TEACHERS ADDED SUCCESFULLY"},200)
    