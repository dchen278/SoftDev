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



# Warmup 2


def string_times(str, n):
    result = ""
    i = 0
    while i < n:
        result += str
        i += 1
    return result


print(string_times('Hi', 2))
print(string_times('Hi', 3))
print(string_times('Hi', 1))

print("-------------------")


def string_splosion(str):
    index = 0
    result = ""
    while index < len(str):
        result += str[:index+1]
        index += 1
    return result

def array_front9(nums):
  rangeNum = len(nums)
  if len(nums) > 4:
    rangeNum = 4
  for num in range(rangeNum):
    if nums[num] == 9:
        return True
  return False
    
print(array_front9([1, 2, 9, 3, 4]))
print(array_front9([1, 2, 3, 4, 9]))
print(array_front9([1, 2, 3, 4, 5]))

print("-------------------")

def front_times(str, n):
  result = ""
  target = ""
  if len(str) < 3:
    target = str
  else:
    target = str[:3]
  for _ in range(n):
    result += target
  return result

print(front_times('Chocolate', 2)) 
print(front_times('Chocolate', 3))
print(front_times('Abc', 3))

print("-------------------")



