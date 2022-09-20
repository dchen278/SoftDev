def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[-1]

print(same_first_last([1, 2, 3]))
print(same_first_last([1, 2, 3, 1]))
print(same_first_last([1, 2, 1]))