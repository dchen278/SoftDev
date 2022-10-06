# Karen Shekyan
# SoftDev
# Oct 6, 2022

from flask import Flask
app = Flask(__name__) # Initialize app to an instance of Flask

@app.route("/") # Function decorator; hello_world() belongs to this route
def hello_world():
    print(__name__) # Print the name of the Python module being run
    return "No hablo queso!"  # Outputs this string to route

app.run()  # Runs app?
