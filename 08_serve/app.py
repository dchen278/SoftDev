"""
David Chen, Kevin Li, Karen Shekyan
The Great Kidding Scuba-Doo Divers
SoftDev
Oct 6, 2022
"""

from flask import Flask
import random
app = Flask(__name__) #create instance of class Flask

# @app.route("/")       #assign fxn to route
# def TNPG():
#     return """# David Chen, Kevin Li, Karen Shekyan
# # SoftDev
# # Oct 6, 2022"""

file = open("occupations.csv", "r")
dictionary = {}
#the dictionary below is for testing purposes
count = {}
#readline twice to ignore the first line: 'Job Class,Percentage'
line = file.readline()
line = file.readline()
#parse the file to create dictionaries
while line:
    strings = line.split(",")
    job_class = ""
    #job classes with commas in them are put back together
    for i in range(len(strings)-1):
        strings[i] = strings[i].strip('"')
        job_class += strings[i]
    #update dictionary with data
    dictionary[job_class] = float(strings[-1])
    count[job_class] = 0
    line = file.readline()
#remove 'Total' after parsing file, putting its value in a separate variable
total = dictionary['Total']
del dictionary['Total']
del count['Total']


def pickJob(job_percentages):
    #generate random number in range
    random_percent = random.uniform(0, total)
    #get list of keys
    jobs = list(job_percentages.keys())
    #subtract each job class's percentage until random number <= 0, them return
    for job in jobs:
        random_percent -= job_percentages.get(job)
        if (random_percent <= 0):
            return job

@app.route("/")
def main():
    print(__name__)
    # return pickJob(dictionary)
    string = """David Chen, Kevin Li, Karen Shekyan <br/>
The Great Kidding Scuba-Doo Divers <br/> <br/>"""
    string += pickJob(dictionary) + "<br/><br/>"
    key_list = list(dictionary.keys())
    for job in key_list:
        string += job + ", " + str(dictionary[job]) + "<br/>"
    string += "============================<br/> Total: " + str(total)
    return string

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
