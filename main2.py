from flask import Flask, render_template,request,session,flash
import sqlite3 as sql
import os
import cv2
from matplotlib import pyplot as plt
import logging
import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
logger = logging.getLogger(__name__)

MIN_MATCH_COUNT = 10
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route('/')
def home():
   return render_template('home.html')

@app.route('/gohome')
def homepage():
    return render_template('index.html')


@app.route('/signup')
def new_user():
   return render_template('signup1.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['Name']
            phonno = request.form['MobileNumber']
            email = request.form['email']
            unm = request.form['Username']
            passwd = request.form['password']
            with sql.connect("gendb.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO user(name,phono,email,username,password)VALUES(?, ?, ?, ?,?)",(nm,phonno,email,unm,passwd))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("login.html", msg=msg)
            con.close()

@app.route('/login')
def user_login():
   return render_template("login.html")

@app.route('/logindetails',methods = ['POST', 'GET'])
def logindetails():
    if request.method=='POST':
            usrname=request.form['username']
            passwd = request.form['password']

            with sql.connect("gendb.db") as con:
                cur = con.cursor()
                cur.execute("SELECT username,password FROM user where username=? ",(usrname,))
                account = cur.fetchall()

                for row in account:
                    database_user = row[0]
                    database_password = row[1]
                    if database_user == usrname and database_password==passwd:
                        session['logged_in'] = True
                        return render_template('index.html')
                    else:
                        flash("Invalid user credentials")
                        return render_template('login.html')


@app.route('/logindeta')
def logindeta():
    return render_template("info.html")

@app.route('/logindeta4')
def logindeta4():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel\Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("StudentDetails\StudentDetails.csv")
    cam = cv2.VideoCapture(1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "Attendance\Attendance_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    print(attendance)
    res = attendance
    #message2.configure(text=res)
    return render_template('resultpred.html', prediction=res)
    #return render_template("info.html")


@app.route('/predict',methods = ['POST', 'GET'])
def predict12():
    if request.method=='POST':

        comment2 = request.form['comment2']

        if comment2 == 'Create New Dataset':

        #os.system('python train.py')
            def is_number(s):
                try:
                    float(s)
                    return True
                except ValueError:
                    pass

                try:
                    import unicodedata
                    unicodedata.numeric(s)
                    return True
                except (TypeError, ValueError):
                    pass

                return False
            def TakeImages():
                name = request.form['comment']
                Id = str(request.form['comment1'])
                print('name',name)
                print('Id',Id)
                if (is_number(Id) and name.isalpha()):
                    cam = cv2.VideoCapture(1)
                    harcascadePath = "haarcascade_frontalface_default.xml"
                    detector = cv2.CascadeClassifier(harcascadePath)
                    sampleNum = 0
                    #a='reach1'

                    while (True):
                        ret, img = cam.read()
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = detector.detectMultiScale(gray, 1.3, 5)
                        for (x, y, w, h) in faces:
                            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        # incrementing sample number
                            sampleNum = sampleNum + 1
                        # saving the captured face in the dataset folder TrainingImage
                            cv2.imwrite("TrainingImage\ " + name + "." + Id + '.' + str(sampleNum) + ".jpg",
                                    gray[y:y + h, x:x + w])
                        # display the frame
                            cv2.imshow('frame', img)
                    #print('reach1', a)
                    # wait for 100 miliseconds
                        if cv2.waitKey(100) & 0xFF == ord('q'):
                            break
                    # break if the sample number is morethan 100
                        elif sampleNum > 30:
                            break
                    cam.release()
                    cv2.destroyAllWindows()
                    res = "Images Saved for ID : " + Id + " Name : " + name
                    row = [Id, name]
                    with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow(row)
                    csvFile.close()
                    #message.configure(text=res)



            TakeImages()
            res = 'New Person Photo is ready to train'
            return render_template('resultpred.html', prediction=res)
        elif comment2 == 'Train Dataset':
            def getImagesAndLabels(path):
                # get the path of all the files in the folder
                imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
                # print(imagePaths)

                # create empth face list
                faces = []
                # create empty ID list
                Ids = []
                # now looping through all the image paths and loading the Ids and the images
                for imagePath in imagePaths:
                    # loading the image and converting it to gray scale
                    pilImage = Image.open(imagePath).convert('L')
                    # Now we are converting the PIL image into numpy array
                    imageNp = np.array(pilImage, 'uint8')
                    # getting the Id from the image
                    Id = int(os.path.split(imagePath)[-1].split(".")[1])
                    # extract the face from the training image sample
                    faces.append(imageNp)
                    Ids.append(Id)
                return faces, Ids

            recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            faces, Id = getImagesAndLabels("TrainingImage")
            recognizer.train(faces, np.array(Id))
            recognizer.save("TrainingImageLabel\Trainner.yml")
            res = "Image Trained"  # +",".join(str(f) for f in Id)
            #message.configure(text=res)
            return render_template('resultpred.html', prediction=res)



if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
