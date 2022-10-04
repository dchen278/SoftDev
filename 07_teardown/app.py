""" 
David Chen, Diana Akhmedova, Sam Cowan
SoftDev
07
2022-10-03
time spent: 

DISCO:

QCC:
0. javascript, golang
1. "/" means the base path 
2. this will print to console
3. __main__
4. this will only be returned on the / route on localhost because the app returns not found on other paths and cannot be accessed via ip and port
5. javascript; express.js
...

INVESTIGATIVE APPROACH:
    - Try running the code and clicking the link and trying other paths other than /
"""

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?