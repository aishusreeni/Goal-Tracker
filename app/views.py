from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Aishwarya!'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route('/food')
def food():
    user = {'nickname': 'Aishwarya!'}
    return render_template('food.html',
                           title='Home',
                           user=user)

@app.route('/exercise')
def exercise():
    user = {'nickname': 'Aishwarya!'}
    return render_template('exercise.html',
                           title='Home',
                           user=user)

@app.route('/skin')
def skin():
    user = {'nickname': 'Aishwarya!'}
    return render_template('skin.html',
                           title='Home',
                           user=user)

@app.route('/health')
def health():
    user = {'nickname': 'Aishwarya!'}
    return render_template('health.html',
                           title='Home',
                           user=user)

@app.route('/read')
def read():
    user = {'nickname': 'Aishwarya!'}
    return render_template('read.html',
                           title='Home',
                           user=user)
