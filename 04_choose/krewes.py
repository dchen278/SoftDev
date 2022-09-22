""" 
David Chen, Diana Akhmedova, Sam Cowan
SoftDev
04_choose
2022-09-22
time spent: 

DISCO: 
 - random.choice returns a random element from given sequence
 - dictionary stores keys and values and allows us to reference them by key

QCC:
 - are these pseudorandom?
 - what does pseudorandom numbers entail?

OPS SUMMARY:
 - we used random from python to return a devo from krewes
"""

import random
import math

krewes = {2: ["hwang30", "wliu30", "iyeung30"],
          7: ["dchen30", "dakhmedova30", "scowan30"],
          8: ["sho30", "dhe30", "mmori30"]
          }

def chooseDevo():
    randomPd = random.choice([2,7,8])
    data = krewes[randomPd]
    return data[random.randint(0, len(data) - 1)]

def chooseDevoRandom():
    periods = [2, 7, 8]
    randomPd = periods[math.floor(random.random() * 3)]
    data = krewes[randomPd]
    return data[math.floor(random.random() * len(data))]

print(chooseDevo())
print(chooseDevoRandom())