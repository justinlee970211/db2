from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request,redirect,url_for

import pymysql
import json
import random


app = Flask(__name__)


@app.route('/monitor/%2520%25E8%258E%25B7%25E5%258F%2596%25E8%25B7%25B3%25E8%25BD%25AC%25E4%25B9%258B%25E5%2589%258D%25E7%259A%2584%25E9%25A1%25B5%25E9%259D%25A2&rsv_pq=c55d03710000b37e&rsv_t=2d7cMpKaY1KiWYx%2Bz5t1b6GhIKMeXL1TJ5SqOd7oVlEOC8FgssuhC%2FEMl7s&rqlang=cn&rsv_enter=0&inputT=2051&rsv_sug3=56&rsv_sug1=12&rsv_sug7=000&rsv_sug2=0&rsv_sug4=2926&rsv_sug=1/')

def index():
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='lzx150909',
        db='db',
        charset='utf8'
    )

    cursor = conn.cursor()
    res = cursor.execute("select * from DBtable")
    u = cursor.fetchall()
    return render_template('monitor.html', u=u)

@app.route('/data/')

def flash():

    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='lzx150909',
        db='db',
        charset='utf8'
    )

    cursor = conn.cursor()
    res = cursor.execute("select * from DBtable")
    u = cursor.fetchall()

    a = u[-1]
    dbdata = {'db': float(a[1].split()[0]), 'date':a[2]}
    return jsonify(dbdata)


@app.route('/')

def dblogin():
    return render_template('login.html')


@app.route('/post/',methods=["POST"])
def dbpost():
    if request.method=='POST':
        name=request.form['name']
        passwd = request.form['passwd']
        print(name,passwd)
        if(name == 'lizixiang' and passwd == '150909'):
            return redirect(url_for('index'))
        else:
            return redirect(url_for('dblogin'))


@app.route('/test/')

def bootstrap():
    return render_template('test.html')

@app.route('/test2/')

def bootstrap2():
    return render_template('test2.html')

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)

