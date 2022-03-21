from flask import Flask, redirect, render_template, request
from users import User
app = Flask(__name__)

@app.route('/users')
def users():
    users = User.get_all()
    return render_template('users.html', users=users)

@app.route('/users/new')
def new_user_form():
    return render_template('new_user.html')

@app.route('/user/create', methods=['POST'])
def create_user():
    print(request.form)
    User.create(request.form)
    return redirect('/users')

if __name__== '__main__':
    app.run(debug=True)