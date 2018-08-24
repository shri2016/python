from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>/age/<int:age>')
def user_info(username, age):
   return 'User %s: Age: %d' % (username, age)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
