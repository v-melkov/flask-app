from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print(i)
    return 'Hello world'

@app.route('/contact/')
@app.route('/feedback/')
def contact():
    return 'Its working'

@app.route('/user/<id>/')
def user_id(id):
    return f'Your user id is {id}'

if __name__ == '__main__':
    app.run(debug=True)
