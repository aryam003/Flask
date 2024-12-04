from flask import Flask,render_template,request
import sqlite3

app=Flask(__name__)


@app.route('/')
def fun():
    return "welcome"

@app.route('/fun1',methods=['POST','GET'])
def fun1():
    if request.method=='POST':
        name =request.form['name']
        place =request.form['place']
        print(name,place)
        con=sqlite3.connect('flaskform.db')
        # con.execute("create table form(name text,place text)")
        # print('table exists.')    
        con.execute("insert into form(name,place)values(?,?)",(name,place))
        con.commit()

    a=20
    return render_template('index.html',data=a)

app.run()