from flask import Flask
from flask import request

# crear instancia
app = Flask(__name__)


# router
@app.route('/')
def index():
    return 'hola'

# /params?p1=hola
@app.route('/params')
def params():
    param = request.args.get('p1', 'no hay nada')
    return 'Params - p1: {} '.format(param)

# configs
HOST = '0.0.0.0'
PORT = 8000
DEBUG = True

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
