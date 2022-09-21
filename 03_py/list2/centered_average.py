def centered_average(nums):
  sum = 0
  for i in range(len(nums)):
    sum += nums[i]
  sum = sum - max(nums) - min(nums)
  return sum / (len(nums) - 2)