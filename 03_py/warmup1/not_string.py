def not_string(str):
  if(str[:3] == "not"):
    return str
  else: 
    return "not " + str

print(not_string('candy'))
print(not_string('x'))
print(not_string('not bad'))