# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
    index = 0
    result = ""
    while index < len(str):
        result += str[:index+1]
        index += 1
    return result

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))