def max_end3(nums):
  maxNum = max(nums[0], nums[2])
  for i in range(3):
    nums[i] = maxNum
  return nums


