# -*- coding: utf-8 -*-

from flask import Flask,url_for,render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html',title=u'TROJANDATA')\

@app.route('/course')
def course():
    return render_template('course.html',title=u'HOW DID I BUILD MY WEBSITE?')

@app.route('/about')
def about():
    return render_template('about.html',title=u'ABOUT')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
