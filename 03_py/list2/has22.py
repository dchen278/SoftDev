def has22(nums):
  bool = False
  for i in range(len(nums) - 1):
    if nums[i] == 2 and nums[i + 1] == 2:
        bool = True
  return bool