from flask import Flask, render_template
# from flask.templating import render_template
from markupsafe import escape

app = Flask(__name__)

greeting = 'heey'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'post  {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the sabbath after /path/
    return 'Sabpath %s' % escape(subpath)


@app.route('/')
def index():
    return '<H1><b><i>index !!!!!!</i></b></H1>'


@app.route('/aaa')
def aaa():
    return render_template("a.html")


@app.route('/' + greeting)
def hello():
    return '<H1><b><i>Hello, World !!!!!!</i></b></H1>'


if __name__ == '__main__':
    app.run(debug=True)
