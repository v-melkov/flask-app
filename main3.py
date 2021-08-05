from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '', 302, {'location': 'http://127.0.0.1:5000/login'}

@app.route('/login/')
def login_required():
    return 'You must login'

if __name__ == '__main__':
    app.run()