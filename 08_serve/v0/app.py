# David Chen, Kevin Li, 
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) # create an instance of our flask app

@app.route("/") # ...
def hello_world():
    print(__name__) # ...
    return "No hablo queso!"  # ...

app.run()  # ...
                
