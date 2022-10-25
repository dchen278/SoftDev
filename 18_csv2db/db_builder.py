# David Chen, William Guo, Marc Jiang
# Disturbed Window Monsters
# SoftDev
# Oct 25 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="students.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
db.execute("DROP TABLE if exists students")
db.execute("DROP TABLE if exists courses")
#==========================================================

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
c.execute("CREATE TABLE students(name TEXT, age INTEGER, id INTEGER PRIMARY KEY)")
c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)")

with open('students.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        # print(row['name'])  # Access by column header instead of column number
        # print(row['age'])
        # print(row['id'])
        c.execute(f"""INSERT INTO students
                    VALUES("{row['name']}", {row['age']}, {row['id']})
                """)
        
with open('courses.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        c.execute(f"""INSERT INTO courses
                    VALUES("{row['code']}", {row['mark']}, {row['id']})
                """)
# command = ""          # test SQL stmt in sqlite3 shell, save as string
# c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


