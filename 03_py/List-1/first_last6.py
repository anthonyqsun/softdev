def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6

print("first_last6([1,2,6]) expected True: " + str(first_last6([1,2,6])))
print("first_last6([6,1,2,3]) expected True: " + str(first_last6([6,1,2,3])))
print("first_last6([13,6,1,2,3]) expected False: " + str(first_last6([13,6,1,2,3])))

