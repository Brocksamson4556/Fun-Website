"""
Name: Mark RIchardson
10/03/2023
"""
from datetime import date
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/home")
def home():
    """Home Function returns the HTML file titles index"""
    return render_template("index.html",date=date.today())
##indexes html page and passes date variable created in python

@app.route("/page1")
def page1():
    """page 1 Function returns the HTML file titles page 1"""
    return render_template("page1.html",date=date.today())
##indexes html page and passes date variable created in python
@app.route("/page2")
def page2():
    """Page 2 Function returns the HTML file titles page 2"""
    return render_template("page2.html",date=date.today())
##indexes html page and passes date variable created in python
@app.route("/register", methods=["POST","GET"])
def register():
    """Register function that allows user to enter values for create login"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not is_username_valid(username):
            user_name_error = "enter a valid username"

            if not is_password_complex(password):
                error_alert = "Password must be 12 characters long and contain atleast\n" \
                          " 1 symbol and Digit."
                return(error_alert)
                print(error_alert)
                return render_template('register.html', error_alert=error_alert)
            return redirect('login')
    return render_template('register.html')

    ##return  redirect(url_for('home'))+
@app.route("/login", methods=['GET','POST'])
def login():
    """Allows user to login and proceed to home page"""
    if request.method == "POST":
        login_user = request.form['username']
        login_pass = request.form['password']
        return redirect('home')
    return render_template('login.html')

def is_password_complex(password):
    """Sets the requirements for password entered"""
    if len(password) < 12:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in '!@#$%^&*9()_+=-' for char in password):
        return False
    return True
def is_username_valid(username):
    """Checkes username"""
    if len(username) > 4:
        return False
    return True


if __name__ == "__main__":
    app.run(debug=True)
