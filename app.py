import os
from datetime import datetime

from flask import Flask
from flask import request
from flask import render_template

import forms

# crear instancia
app = Flask(__name__)  # por defecto template_folder="templates"


# router
@app.route('/')
def homepage():
	time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
	os_var = os.environ.get('OS_VAR', 'not set')
	return render_template('home.html', time=time, os_var=os_var)


@app.route('/form/')
def index():
    comment_form = forms.CommentForm()
    return render_template('index.html', form=comment_form)

# /params/category/id
@app.route('/params/')
@app.route('/params/<category>/')
@app.route('/params/<category>/<int:id>')
def params(category='default category', id=1):
    return render_template('params.html', category=category, id=id, rango=range(0, id))


# configs
HOST = '0.0.0.0'
PORT = 8000
DEBUG = True

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
