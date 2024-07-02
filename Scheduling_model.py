import mysql.connector
import json
from flask import jsonify, make_response,request
import logging
import psycopg2
import random as rd
import pandas as pd

class Scheduling():
    #connectionn stablishment code
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",username="root",password="caamodel@1",database="mydatabase")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("CONNECTION SUCCESSFULL")
        except:
            print("some error")



    def depart_schedule(self):
                data = request.json
                department = data.pop('department')
                batch = data.pop('batch')
                papers = data.get('papers', [])  
                
                if 'papers' in data and not isinstance(data['papers'], list):
                    return make_response({"message": "Invalid 'papers' format, must be a list"}, 400)
                
                
                query = "SELECT * FROM users WHERE department NOT IN (%s, 'admin')"
                self.cur.execute(query, (department,))
                allowed_teachers = self.cur.fetchall()
                    
                    
                query1 = "SELECT * FROM classrooms"
                self.cur.execute(query1)
                free_classrooms = self.cur.fetchall()
                
                scheduling_result = self.schedule_teachers(allowed_teachers, free_classrooms, department, batch, papers)
                if scheduling_result['success']:
                    return make_response({"message": "All teachers scheduled successfully"}, 200)
                else:
                    return make_response({"message": scheduling_result['message']}, 500)
                    # Function to schedule teachers
    def schedule_teachers(self,teachers, classrooms, department, batch, papers):
        scheduled_teachers = set()
        occupied_classrooms = set()
        success = True
        message = "All teachers scheduled successfully"
        for paper in papers:
            scheduled_for_paper = False
            for teacher in teachers:
                if teacher['department'] != department and teacher['id'] not in scheduled_teachers:
                    for classroom in classrooms:
                        if classroom['Room_number'] not in occupied_classrooms:
                            query = """
                            INSERT INTO schedulings 
                            (teacher_id, department, name, freehourstoday, Builduing, Floor, Room_number, paper_depart, Subject, batch) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """
                            values = (
                                teacher['id'], 
                                teacher['department'], 
                                teacher['name'], 
                                teacher['freehourstoday'], 
                                classroom['Builduing'], 
                                classroom['Floor'], 
                                classroom['Room_number'], 
                                department, 
                                paper, 
                                batch
                            )
                            try:
                                self.cur.execute(query, values)
                                scheduled_teachers.add(teacher['id'])
                                occupied_classrooms.add(classroom['Room_number'])
                                scheduled_for_paper = True
                                break  
                            except psycopg2.Error as e:
                                print(f"Error executing query: {e}")
                                self.cur.rollback()
                                success = False
                                message = f"Error scheduling teacher {teacher['id']} for paper {paper} in classroom {classroom['Room_number']}"
                                break
                        if scheduled_for_paper:
                            break  
        self.cur.execute("SELECT * FROM schedulings")
        result_file = self.cur.fetchall()
        print(result_file)   
        df = pd.DataFrame(result_file)
        df.to_excel("TimeTable(CS).xlsx", index=True)
        print("Excel file 'TimeTable(CS).xlsx' created successfully.")
        self.cur.execute(f"TRUNCATE TABLE schedulings")
        return {"success": success, "message": message}                          

