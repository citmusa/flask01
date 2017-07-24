from flask import Flask

# crear instancia
app = Flask(__name__)


# router
@app.route('/')
def index():
    return 'hola'


# configs
HOST = '0.0.0.0'
PORT = 8000
DEBUG = True

app.run(host=HOST, port=PORT, debug=DEBUG)
