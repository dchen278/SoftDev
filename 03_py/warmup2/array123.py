def array123(nums):
  return (1 in nums) and (2 in nums) and (3 in nums)


print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))