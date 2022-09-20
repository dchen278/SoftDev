def string_match(a, b):
  times = min(len(a), len(b))
  i = 0
  result = 0
  while i < times - 1:
    if a[i:i+2] == b[i:i+2]:
        result += 1
    i+=1
  return result

print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))