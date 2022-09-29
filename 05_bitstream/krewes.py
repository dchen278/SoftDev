""" 
Team Don't Worry
David Chen, William Guo
SoftDev
05_bitstream
2022-09-28
time spent: 0.9 hours

DISCO: 
    - We can use dict.values() and dict.keys() to get a list of a dict's values and keys respectively
    - We can use f strings to interpolate variables without concatenating using +
QCC:
    - N/A

"""

import random
import math
import io

# krewes = {
#     2: [{'NICHOLAS': 'EUGENE'}, {'ANTHONY': 'EUGENE'}], 
#     7: [{'ANTHONY': 'EUGENE'}, {'ANTHONY': 'EUGENE'}], 
#     8: [{'NICHOLAS': 'EUGENE'}, {'NICHOLAS': 'EUGENE'}]
# }


with io.open("./krewes.txt", 'r', encoding='utf8') as f:
    krewes_data = f.read()
    f.close()

krewes = {2: [], 7: [], 8: []}

devo_list = krewes_data.split("@@@")

for devo in devo_list:
    info = devo.split("$$$")
    print(info)
    krewes[int(info[0])].append({info[1]: f"{info[2]}"})

print(f"krewes: {krewes} \n")


def choose_devo_with_rand_int():
    periods = [2, 7, 8]
    random_period = periods[random.randint(0, len(periods) - 1)]
    data = krewes[random_period]
    devo_data = data[random.randint(0, len(data) - 1)]
    print(f"Period: {random_period}")
    print(f"Random Devo: {list(devo_data.keys())[0]}")
    print(f"Duckie: {list(devo_data.values())[0]}")


def choose_devo_with_choice():
    random_period = random.choice([2, 7, 8])
    data = krewes[random_period]
    devo_data = random.choice(data)
    print(f"Period: {random_period}")
    print(f"Random Devo: {list(devo_data.keys())[0]}")
    print(f"Duckie: {list(devo_data.values())[0]}")


def choose_devo_with_random():
    periods = [2, 7, 8]
    random_period = periods[math.floor(random.random() * len(periods))]
    data = krewes[random_period]
    devo_data = data[math.floor(random.random() * len(data))]
    print(f"Period: {random_period}")
    print(f"Random Devo: {list(devo_data.keys())[0]}")
    print(f"Duckie: {list(devo_data.values())[0]}")


print("RANDOM.RANDINT:")
choose_devo_with_rand_int()
print("\nRANDOM.CHOICE:")
choose_devo_with_choice()
print("\nRANDOM.RANDOM:")
choose_devo_with_random()
