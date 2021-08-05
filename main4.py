from flask import Flask, request, render_template, redirect, url_for, flash, make_response
from forms import ContactForm

# from jinja2 import Template


app = Flask(__name__)

@app.route('/')
def index():
    name, age, profession = 'Jerry', 25, 'Cat'
    template_context = dict(name=name, age=age, profession=profession)
    return render_template('index.html', **template_context)

@app.route('/user/<int:user_id>')
def user_id(user_id):
    return f"Your user-id is: {user_id}"

@app.route('/books/<genre>/')
def books(genre):
    return f'All books by genre {genre}'

@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    username = ''
    password = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

    if username == 'root' and password == 'pass':
        message = "Correct username and password"
    else:
        message = "Wrong username and password"

    return render_template('login.html', message=message)

@app.route('/contact/', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        print(name, email, message, sep=" ")
        print('\n\nData received. Redirecting')
        flash('Message received', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)

@app.route('/cookie/')
def cookie():
    if not request.cookies.get('foo'):
        res = make_response('Setting a cookie')
        res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
    else:
        res = make_response('Value of cookie foo is {}'.format(request.cookies.get('foo')))
    return res

if __name__ == '__main__':
    app.debug = True
    app.config['SECRET_KEY'] = 'a really really really really long secret key'
    app.run(debug=True)