# Spicy Vanilla: Matthew Yee, Jeremy Kwok, David Chen
# SoftDev
# K20 -- REST APIs
# 2022-11-21
# time spent: 1 hours

from flask import Flask  # facilitate flask webserving
from flask import render_template  # facilitate jinja templating
from flask import request  # facilitate form submission
import requests
import json

app = Flask(__name__)  # create Flask object

f = open("key_nasa.txt", "r")
key = f.read()

# Set the secret key to some random bytes. Keep this really secret!
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET', 'POST'])
def main():
    # key = "INSERT KEY HERE" #implement reading of key_nasa.txt?
    response = requests.get(
        f"https://api.nasa.gov/planetary/apod?api_key={key}")
    # print(response.status_code) # 200 means the request succeeded

    # print(response.json()) #prints JSON response from API call

    # text = json.dumps(response.json(), sort_keys=True, indent = 4) #formats JSON output into something more human-readable
    # print(text)

    temp = response.json()
    # print(temp["url"])
    image = temp["url"]
    text = temp["explanation"]
    # print(image)
    # print(text)

    return render_template('main.html', image=image, text=text)


if __name__ == "__main__":  # false if this file imported as module
    # enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
