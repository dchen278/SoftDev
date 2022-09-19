# Given an array of ints, return True if one of the first 4 elements in the array is a 9.
# The array length may be less than 4.

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