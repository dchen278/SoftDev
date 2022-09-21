def sum67(nums):
  bool = False
  sum = 0
  for i in range(len(nums)):
    if nums[i] != 6 and not bool:
        sum += nums[i]
    elif nums[i] == 7:
        bool = False
    else:
        bool = True
  return sum