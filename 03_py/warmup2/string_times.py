# Given a string and a non-negative int n,
# return a larger string that is n copies of the original string.

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
