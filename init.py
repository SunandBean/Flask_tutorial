from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# @app.route('/')
# def index():
#     return "Hello Flask"

# @app.route('/', methods=['GET','POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Try again'
#         else:
#             return redirect(url_for('secret'))
#     return render_template('index.html',error=error)
#
# @app.route('/secret')
# def secret():
#     return "Secret"

# @app.route('/')
# def index():
#     return 'Index Page'
#
# @app.route('/hello')
# def hello():
#     return 'Hello World!'
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

if __name__ == "__main__":
    app.run()