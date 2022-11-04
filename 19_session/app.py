# David Chen, William Guo, Marc Jiang
# Disturbed Window Monsters
# SoftDev
# Nov 03 2022


from flask import Flask  # facilitate flask webserving
from flask import render_template  # facilitate jinja templating
from flask import request, Response, redirect, session, url_for  # facilitate form submission

# the conventional way:
#from flask import Flask, render_template, request
username = "DWM"
password = "ABC"

app = Flask(__name__)  # create Flask object
app.secret_key = "m4Wa0SY66R34R2fbty7P5Nmxg8fLNOQ6"

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)  # displays app
    print("***DIAG: request obj ***")
    print(request)  # displays page request
    print("***DIAG: request.args ***")
    print(request.args)
    # print("***DIAG: request.args['username']  ***")
    # print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    if "username" in session:
        return render_template('response.html', status="Successful")
    else:
        return render_template('login.html')


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    if request.method == "GET":
        if "username" in session:
            return render_template('response.html', status="Successful")
        else:
            return render_template('login.html')
    elif request.method == "POST":
        print("\n\n\n")
        print("***DIAG: this Flask obj ***")
        print(app)
        print("***DIAG: request obj ***")
        print(request)
        print("***DIAG: request.args ***")
        print(request.form)  # displays entered info as dict
        print("***DIAG: request.args['username']  ***")
        print(request.form['username'])
        print("***DIAG: request.headers ***")

        if request.form['username'] == username and request.form['password'] == password:
            session["username"] = request.form.get("username")
            return render_template('response.html', status="Successful")
        elif request.form['username'] != username and request.form['password'] != password:
            return render_template('response.html', status="Incorrect Username and Password")
        elif request.form['username'] != username:
            return render_template('response.html', status="Incorrect Username")
        elif request.form['password'] != password:
            return render_template('response.html', status="Incorrect Password")
        return f"Waaaa hooo HAAAH {request.form['username']}"  # response to a form submission
    else:
        return Response(status=405)

@app.route("/logout", methods=['POST'])
def logout():
    if request.method != "POST":
        return Response(status=405)
    print(request.form)  # displays entered info as dict
    if "username" in session:
        session.pop("username")
    return redirect("/auth")



if __name__ == "__main__":  # false if this file imported as module
    # enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
