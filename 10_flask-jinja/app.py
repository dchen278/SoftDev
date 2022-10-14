# David Chen
# SoftDev
# Oct 13, 2022

# Q0: What will happen if you remove render_template from this line? (log your prediction before you pull the trigger...)
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "No hablo queso!"


coll = [0, 1, 1, 2, 3, 5, 8]


# Q1: Can all of your teammates confidently predict the URL to use to load this page?
@app.route("/my_foist_template")
def test_tmplt():
    # Q2: What is the significance of each argument? Simplest, most concise answer best.
    return render_template('model_tmplt.html', foo="fooooo", collection=coll)


@app.route("/foo")
def test():
    return render_template("foo.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
