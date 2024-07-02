import _mysql_connector
import mysql.connector
import json
from flask import jsonify, make_response, request


class classrooms():

    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",username="root",password="caamodel@1",database="mydatabase")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("CONNECTION SUCCESSFULL")
        except:
            print("some error")

    def classrooms_getall_model(self):
        #query execution code
        self.cur.execute("SELECT * FROM classrooms")
        resulte = self.cur.fetchall()
        if len(resulte)>0:
            return make_response({"CLASS ROOM DETAILS " : resulte},200)
        else:
            return make_response({"MESSAGE ":"NO DATA FIND"},204)
        
    def classrooms_addone_model(self):
        data = request.json
        #query execution code
        self.cur.execute(f"INSERT INTO classrooms(Builduing, Floor, Room_number) VALUES('{data['Builduing']}', '{data['Floor']}', '{data['Room_number']}')")
        return make_response({"message" : "CLASSROOM ADDED SUCCESFULLY"},200)
    
    def classrooms_patch_model(self):
        data = request.json
        if not data or  'Room_number' not in data:
            print(data)
            return jsonify({"error": "Missing 'Room_nnumber' in request body"}), 400
        Room_number = data.pop('Room_number')

        qry = "UPDATE classrooms SET "
        for key in data:
            qry = qry + f"{key} = '{data[key]}',"
        
        qry = qry[:-1] + f" WHERE Room_number={Room_number}"
        self.cur.execute(qry)
        if self.cur.rowcount>0:
            return ("Specific couloumn of the table has been updated")
        else:
            return("ERROR")

    def classrooms_delete_model(self):
        data = request.json
        Room_number = data.pop('Room_number')

        if not Room_number:
            return jsonify({"error": "Missing 'Room_number' in request body"}), 400
        try:
            self.cur.execute("DELETE FROM classrooms WHERE Room_number = %s", (Room_number,))
            if self.cur.rowcount > 0:
                return make_response({"message": "Classroom DELETED SUCCESSFULLY"}, 200)
            else:
                return make_response({"message": "NOTHING TO DELETE"}, 202)
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            return make_response({"message": "An error occurred while deleting the classroom"}, 500)

                