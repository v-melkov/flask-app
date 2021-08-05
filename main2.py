from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/user/<int:user_id>/')
def user_id(user_id):
    return f'Your user id is {user_id}'

@app.route('/books/<genre>/')
def books(genre):
    return f'All books by genre {genre}'

if __name__ == '__main__':
    app.run(debug=True)