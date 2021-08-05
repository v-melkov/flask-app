from flask import Flask, request, g, abort

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    print('before_first_request called')

@app.before_request
def before_request():
    print('before request called')

@app.after_request
def after_request(response):
    print('after request called')
    return response

@app.errorhandler(404)
def http_404_handler(error):
    return '<p>http 404 error</p>'

@app.errorhandler(500)
def http_500_handler(error):
    return '<p>http 500 error</p>'

@app.route('/')
def index():
    # print('index called')
    # return '<p>Testing Request hooks</p>'
    abort(404)

if __name__ == '__main__':
    app.run(debug=True)