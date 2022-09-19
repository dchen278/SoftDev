# Given a string and a non-negative int n,
# we'll say that the front of the string is the first 3 chars,
# or whatever is there if the string is less than length 3.
# Return n copies of the front.

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