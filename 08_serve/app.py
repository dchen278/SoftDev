'''
Karen Shekyan, David Chen, Kevin Li
The Great Kidding Scuba-Doo Divers
SoftDev
Oct 6, 2022
'''

from flask import Flask
import random
app = Flask(__name__)

#initialize file and dictionary
file = open("occupations.csv", "r")
dictionary = {}

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
    line = file.readline()

#remove 'Total' after parsing file, putting its value in a separate variable
total = dictionary['Total']
del dictionary['Total']


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
    #print __name__ to terminal
    print(__name__)
    job_choice = pickJob(dictionary)
    #create big string to output
    #add names and TNPG
    string = """<h1>The Great Kidding Scuba-Doo Divers</h1>
    <h2>David Chen, Kevin Li, Karen Shekyan</h2> <br/>"""
    #add job choice
    string += f"<h3>Job choice: </h3> <a href='https://www.google.com/search?q={job_choice}'>{job_choice}<a/> <br/><br/><br/>"

    #create table to display jobs and weights
    string += """<h3>Jobs table: </h3>
    <table> <tr> <th> Job Class </th> <th> Percentage </th> </tr>"""
    #add jobs and their weights
    key_list = list(dictionary.keys())
    for job in key_list:
        string += "<tr> <td>" + job + "</td> <td> " + str(dictionary[job]) + "</td> </tr>"

    #show total information for table of jobs
    string += "<tr> <th> Total: </th> <th>" + str(total) + "</th> </tr> </table>"
    #output the string
    return string

#run main in debug mode
if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
