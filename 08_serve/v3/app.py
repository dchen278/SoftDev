# Karen Shekyan
# SoftDev
# Oct 6, 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go? #This prints to the terminal
    return "No hablo queso!"

app.debug = True
app.run()

'''
debug causes the page to be reloaded when code is changed, but crashes if there
are syntax errors
'''
