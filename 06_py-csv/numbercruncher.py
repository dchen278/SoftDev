""" 
Team Don't Worry
David Chen, William Guo
SoftDev
06_py-csv
2022-09-29
time spent:

DISCO: 
    - You don't need to import io to read files
    - You can pass weights into random.choices
QCC:
    - N/A

"""
import random
import math

with open("./occupations.csv", 'r', encoding='utf8') as f:
    occupation_data = f.read()
    f.close()

occupation_list = occupation_data.split("/n")

