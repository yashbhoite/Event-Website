import sqlite3
from flask import Flask,render_template,request
import os

THIS_FOLDER= os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/signup')
def signup():
    return render_template('regsitration.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


@app.route('/register',methods=['post'])
def register():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    username = request.form['username']
    phone = request.form['phone']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    x = cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    x = cursor.fetchall()
    if password!= confirm_password:
        return render_template('regsitration.html',message="Password do not match",first_name=first_name,last_name=last_name,email=email,username=username,phone=phone)

    elif int(len(x)) > 0:
        return render_template('regsitration.html',message="That username is already taken, please choose another")
       
    else:
        connection = sqlite3.connect('database.db')
        my_cursor = connection.cursor()
        my_cursor.execute("INSERT INTO users VALUES(?,?,?,?,?,?)",(first_name,last_name,email,username,phone,password))
        connection.commit()
        my_cursor.close()
        return render_template('login.html',message="You have successfully registered")
        
@app.route('/loginconfirm' ,methods=['POST'])
def loginconfirm():
    username = request.form['username']
    password = request.form['password']
    connection = sqlite3.connect('database.db')
    my_cursor = connection.cursor()
    my_cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username,password))
    details = my_cursor.fetchall()
    connection.commit()
    my_cursor.close()
    if(len(details) == 0):
        return render_template('login.html',message="Invalid username or passowrd")
    else:
        return render_template('quiz.html',user=username)


if(__name__) == '__main__':
    app.run(debug=True)