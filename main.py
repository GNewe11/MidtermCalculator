from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def instructions():
    return render_template("instructions.html")

@app.route('/add/<num1>/<num2>')
def addNums(num1, num2):
    num3 = num1 + num2
    return render_template("addNums.html", numb1=num1, numb2=num2)

@app.route('/sub/<num1>/<num2>')
def subNums(num1, num2):
    num3 = num1 - num2
    return render_template("subNums.html", numb1=num1, numb2=num2)

@app.route('/mult/<num1>/<num2>')
def multNums(num1, num2):
    num3 = num1 * num2
    return render_template("multNums.html", numb1=num1, numb2=num2)

@app.route('/div/<num1>/<num2>')
def divNums(num1, num2):
    num3 = num1 / num2
    return render_template("divNums.html", numb1=num1, numb2=num2)