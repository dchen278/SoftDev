""" 
David Chen, William Guo
SoftDev
05_choose
2022-09-28
time spent: 0.5 hours

DISCO: 

QCC:

OPS SUMMARY:
"""

import random
import math
import io

with io.open("./krewes.txt",'r',encoding='utf8') as f:
    krewesData = f.read()

krewes = {2: [], 7: [], 8: []}

devoList = krewesData.split("@@@")

for devo in devoList:
    info = devo.split("$$$")
    print(info[0])
    krewes[int(info[0])].append({info[1]: f"{info[2]}"})

print(krewes)

def chooseDevoWithRandInt():
    periods = [2, 7, 8]
    randomPd = periods[random.randint(0, len(periods) - 1)]
    print("Random Period: ", randomPd)
    data = krewes[randomPd]
    return data[random.randint(0, len(data) - 1)]


def chooseDevoWithChoice():
    randomPd = random.choice([2, 7, 8])
    print("Random Period: ", randomPd)
    data = krewes[randomPd]
    return random.choice(data)


def chooseDevoWithRandom():
    periods = [2, 7, 8]
    randomPd = periods[math.floor(random.random() * len(periods))]
    print("Random Period: ", randomPd)
    data = krewes[randomPd]
    return data[math.floor(random.random() * len(data))]


print("RANDOM.RANDINT:")
print("Random Devo: ", chooseDevoWithRandInt())
print("\nRANDOM.CHOICE:")
print("Random Devo: ", chooseDevoWithChoice())
print("\nRANDOM.RANDOM:")
print("Random Devo: ", chooseDevoWithRandom())
