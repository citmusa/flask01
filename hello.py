from flask import Flask
from flask import request

# crear instancia
app = Flask(__name__)


# router
@app.route('/')
def index():
    return 'hola'

# /params/category/id
@app.route('/params/')
@app.route('/params/<category>/')
@app.route('/params/<category>/<int:id>')
def params(category='default category', id=1):
    return 'CAT: {}; ID:{} '.format(category, id)

# configs
HOST = '0.0.0.0'
PORT = 8000
DEBUG = True

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
