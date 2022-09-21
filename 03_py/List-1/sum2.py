def sum2(nums):
  return sum(nums[:min(len(nums),2)])

print("sum2([1,2,3]) expected 3: " + str(sum2([1,2,3])))
print("sum2([1,1]) expected 2: " + str(sum2([1,1])))
print("sum2([1]) expected 1: " + str(sum2([1])))

