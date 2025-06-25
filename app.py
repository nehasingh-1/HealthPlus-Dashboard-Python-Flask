from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db_connection():
    conn = sqlite3.connect('healthplus.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    if 'username' in session:
        conn = get_db_connection()
        patients = conn.execute('SELECT * FROM patients').fetchall()
        conn.close()
        return render_template('dashboard.html', patients=patients)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            session['username'] = username
            return redirect(url_for('index'))
        return 'Invalid Credentials'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/data')
def data():
    conn = get_db_connection()
    health_data = conn.execute('SELECT timestamp, heart_rate, temperature FROM health_metrics').fetchall()
    conn.close()
    return {'data': [dict(row) for row in health_data]}

if __name__ == '__main__':
    app.run(debug=True)