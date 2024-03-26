from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def instructions():
    return render_template("instructions.html")

@app.route('/add/<num1>/<num2>')
def addNums(num1, num2):
    return render_template("addNums.html")

@app.route('/sub/<num1>/<num2>')
def subNums(num1, num2):
    return render_template("addNums.html")

@app.route('/mult/<num1>/<num2>')
def multNums(num1, num2):
    return render_template("addNums.html")

@app.route('/div/<num1>/<num2>')
def divNums(num1, num2):
    return render_template("addNums.html")