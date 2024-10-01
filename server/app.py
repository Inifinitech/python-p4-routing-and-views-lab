#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route("/print/<string:parameter>")
def print_string(parameter):
    # printing the string in the console
    print(parameter)
    # displaying the string in the browser
    return f"{parameter}"

# print every number on its own line in the browser
@app.route("/count/<int:parameter>")
def count(parameter):
    result = "\n".join(str(i) for i in range(parameter)) + "\n"
    return result
    
@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    result = ""
    if operation == '+':
        result = f"{num1 + num2}"
    elif operation == 'div':
        result = f"{num1 / num2}"
    elif operation == '*':
        result = f"{num1 * num2}"
    elif operation == '-':
        result = f"{num1 - num2}"
    elif operation == '%':
        result = f"{num1 % num2}"
    else:
        result


    return result


if __name__ == '__main__':
    app.run(port=5555, debug=True)
