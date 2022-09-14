def sleep_in(weekday, vacation):
    return vacation or not weekday


print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))

print("-------------------")

def diff21(n):
    if n > 21:
        return 2 * abs(n-21)
    return abs(n-21)


print(diff21(19))
print(diff21(10))
print(diff21(21))

print("-------------------")

def near_hundred(n):
    return (abs(n-100) <= 10) or (abs(n-200) <= 10)


print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))

print("-------------------")

def missing_char(str, n):
  return str[0:n] + str[n+1:]

print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))

def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    return (a < 0 and b > 0) or (a > 0 and b < 0)

def front_back(str):
    if len(str) <= 1:
        return str
    return str[-1] + str[1:len(str)-1] + str[0]