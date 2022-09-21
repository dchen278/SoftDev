def rotate_left3(nums):
  first = nums[0]
  nums[0] = nums[1]
  nums[1] = nums[2]
  nums[2] = first
  return nums