from flask import Flask
from flask import request
from flask import render_template

# crear instancia
app = Flask(__name__)  # por defecto template_folder="templates"


# router
@app.route('/')
def index():
    return render_template('base.html')

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
