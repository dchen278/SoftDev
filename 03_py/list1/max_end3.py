def max_end3(nums):
  maxNum = max(nums[0], nums[2])
  for i in range(3):
    nums[i] = maxNum
  return nums



print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
print(max_end3([2, 11, 3]))