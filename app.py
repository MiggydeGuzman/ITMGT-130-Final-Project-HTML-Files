from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template("login.html", page="login")

@app.route('/homepage')
def home():
    return render_template("homepage.html", page="Home Page")

@app.route('/classes')
def classes():
    return render_template("classes.html", page="Classes")

@app.route('/login')
def logout():
    return render_template("login.html", page="Log Out")

@app.route('/classdetails')
def classdetails():
    return render_template("classdetails.html", page="Class Details")

@app.route('/contactus')
def contactus():
    return render_template("contactus.html", page="Contact Us")

@app.route('/myclasses')
def myclasses():
    return render_template("myclasses.html", page="My Classes")

@app.route('/signup')
def signup():
    return render_template("signup.html", page="Sign Up")

@app.route('/myaccount')
def myaccount():
    return render_template("myaccount.html", page="My Account")

@app.route('/updateaccountinformation')
def updateaccountinformation():
    return render_template("updateaccountinformation.html", page="Update Account Information")

if __name__ == '__main__':
    app.run(debug=True)









