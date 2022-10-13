from crypt import methods
from flask import Flask, render_template,request,redirect
import mysql.connector

myapp=Flask(__name__,template_folder="templates")
@myapp.route("/")
def check():
    return render_template("login1.html")

@myapp.route("/",methods =["POST"])
def checklogin():
    UN = request.form['username']
    PW = request.form['password']
    mydb = mysql.connector.connect(host="localhost", user="root", password="Nagamithra*17", database="final_project")
    cursor = mydb.cursor()
    query1 = "SELECT username, Password from signup WHERE Username = '{un}' and Password ='{pw}'".format(un = UN, pw = PW)
    rows = cursor.execute(query1)
    rows = rows.fetchall()
    if len(rows) ==1:
        return render_template("tracker.html")
    else:
        return redirect("/register")
@myapp.route("/register", methods= ["GET" ,"POST"])
def registerpage():
    if request.method == "POST":
        dUN = request.form['Dusername']
        dPW = request.form['Dpassword']
        Uemail = request.form['Emaluser']
        mydb = mysql.connector.connect(host="localhost", user="root", password="Nagamithra*17", database="final_project")
        cursor = mydb.cursor()
        query1 = "INSERT INTO signup VALUES('{u}','{p}','{e}')".format(u=dUN,p=dPW,e=Uemail)
        cursor.execute(query1)
        mydb.commit()
        return redirect("/")
    return render_template("sign_up.html")


myapp.run()