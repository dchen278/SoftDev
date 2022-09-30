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
from operator import indexOf
import random
import math

with open("./occupations.csv", 'r', encoding='utf8') as f:
    occupation_data = f.read()
    f.close()

# initialize variables
occupation_list = occupation_data.split("\n")
occupation_classes = []
occupation_percentages = []

def comma_in_field(row):
    data = row.split('"')
    # print(data)
    percentage = row.split(",") 
    print(percentage[-1])
    return [data[1], percentage[-1]]

for occupation in occupation_list:
    if '"' in occupation:
        data_in_comma = comma_in_field(occupation)
        occupation_classes.append(data_in_comma[0])
        occupation_percentages.append(data_in_comma[1])
    else:
        data = occupation.split(",")
        occupation_classes.append(data[0])
        occupation_percentages.append(data[1])

# remove the labels
occupation_classes.pop(0)
occupation_percentages.pop(0)
occupation_classes.pop(len(occupation_classes)-1)
occupation_percentages.pop(len(occupation_percentages)-1)


# print(occupation_classes)
print(len(occupation_classes))
# print(occupation_percentages)
print(len(occupation_percentages))


print(random.choices(occupation_classes,weights=occupation_percentages))