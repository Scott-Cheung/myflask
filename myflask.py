# -*- coding: utf-8 -*-

from flask import Flask,url_for,render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html',title=u'主页')

@app.route('/about')
def about():
    return render_template('about.html',title=u'关于')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
