#!/usr/local/bin/python3
import mysql.connector
import json
        
class database:
    def __init__(self):
        print("Connected...")
        
    def add_job(self):
        cnx = mysql.connector.connect(user='admin', password='password', host='192.168.1.206', database='resume')
        title = input("Job title: ")
        company = input("Company Name: ")
        s_date = input("Start Date: ")
        e_date = input("End Date: ")
        description = input("Description: ")

        mycursor = cnx.cursor()
        sql = "INSERT INTO jobs (title, company, start_date, end_date, description) VALUES ('{}', '{}', '{}', '{}', '{}');".format(title, company, s_date, e_date, description)
        print(sql)
        mycursor.execute(sql)
        cnx.commit()
        mycursor.close()
        cnx.close()
        
    def print_table(self):
        cnx = mysql.connector.connect(user='admin', password='password', host='192.168.1.206', database='resume')
        mycursor = cnx.cursor()
        sql = "select * from jobs"
        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
        cnx.close()

    def del_job(self):
        cnx = mysql.connector.connect(user='admin', password='password', host='192.168.1.206', database='resume')
        mycursor = cnx.cursor()
        print("Which ID would you like to delete?")
        del_id = input("ID:")
        sql = "DELETE from jobs where id = {}".format(del_id)
        print(sql)
        mycursor.execute(sql)
        cnx.commit()
        mycursor.close()
        cnx.close()

conn = database()
#conn.add_job()
#conn.del_job()
conn.print_table()