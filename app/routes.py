from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ray'}
    posts = [
        {
            'author': {'username': 'Kobe'},
            'body': 'Nice Dunk!!!!'
        },
        {
            'author': {'username': 'Lebron'},
            'body': 'I love AD!!!!'
        }
    ]
    return render_template('index.html', user=user, posts=posts)
