def same_first_last(nums):
  if len(nums) == 0: return False
  return nums[0] == nums[-1]

print("same_first_last([]) expected False: " + str(same_first_last([])))
print("same_first_last([1,2,3]) expected False: " + str(same_first_last([1,2,3])))
print("same_first_last([1,2,3,1]) expected True: " + str(same_first_last([1,2,3,1])))

