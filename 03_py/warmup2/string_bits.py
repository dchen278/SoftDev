# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
  ret = str[0]
  str = str[1:len(str)-1]
  for i in range(len(str)):
    if (str[i] == str[i+1]):
      str = str[i+1:len(str)-1]
    ret += str[i]
  return ret

def string_bits1(str):
  ret = ""
  index = 0
  while index < len(str) - 2:
    

print(string_bits1('Hello'))
print(string_bits1('Hi'))
print(string_bits1('Heeololeo'))