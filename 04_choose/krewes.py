""" 
David Chen, Diana Akhmedova, Sam Cowan
SoftDev
04_choose
2022-09-22
time spent: 0.5 hours

DISCO: 
 - random.choice returns a random element from given sequence.
 - A dictionary stores keys and values and allows us to reference them by key.

QCC:
 - Are these pseudorandom?
 - What does pseudorandom numbers entail?

OPS SUMMARY:
 1. Given krewes = {dict(int : list)}, we randomly chose a period (2, 7, or 8) using random.choice,
    and printed the random period.
 2. We retreived the corresponding list from the randomly selected period
    by setting it to a temporary variable called "data."
 3. We returned a randomly selected Devo by using random.randint.
 4. We also created another function that utilizes random.random and floors the output,
    which essentially achieves the same outcome.
"""

import random
import math

# krewes = {2: ["hwang30", "wliu30", "iyeung30"],
#           7: ["dchen30", "dakhmedova30", "scowan30"],
#           8: ["sho30", "dhe30", "mmori30"]
#           }

krewes = {
           2: ["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY"], 
           7: ["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
           8: ["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "wanying"]
         }

def chooseDevoWithInt():
    randomPd = chooseRandomPd()
    print("Random Period: ", randomPd)
    data = krewes[randomPd]
    return data[random.randint(0, len(data) - 1)]

def chooseRandomPd():
    return random.choice([2, 7, 8])

def chooseDevoWithChoice():
    randomPd = chooseRandomPd()
    print("Random Period: ", randomPd)
    data = krewes[randomPd]
    return random.choice(data)

def chooseDevoWithRandom():
    periods = [2, 7, 8]
    randomPd = periods[math.floor(random.random() * 3)]
    print("Random Period: ", randomPd)
    data = krewes[randomPd]
    return data[math.floor(random.random() * len(data))]

print("RANDOM.RANDINT:")
print("Random Devo: ", chooseDevoWithInt())
print("\nRANDOM.CHOICE:")
print("Random Devo: ", chooseDevoWithChoice())
print("\nRANDOM.RANDOM:")
print("Random Devo: ", chooseDevoWithRandom())