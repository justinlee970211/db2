from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request,redirect,url_for

import pymysql
import json
import random


app = Flask(__name__)


@app.route('/monitor/%2520%25E8%258E%25B7_sug=1/')

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

@app.route('/gauge/')

def bootstrap2():
    return render_template('gauge.html')

@app.route('/test3/')

def bootstrap3():
    return render_template('test3.html')

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)

