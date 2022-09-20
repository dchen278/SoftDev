# Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
  counter = 0
  for i in range(len(nums)):
    if (nums[i] == 9):
      counter += 1
  return counter
    
print(array_count9([1, 2, 9]))
print(array_count9([1, 9, 9]))
print(array_count9([1, 9, 9, 3, 9]))