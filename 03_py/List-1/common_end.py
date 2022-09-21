def common_end(a, b):
  return a[0]==b[0] or a[-1]==b[-1]

print("common_end([1,2,3],[7,3]) expected True: " + str(common_end([1,2,3],[7,3])))
print("common_end([1,2,3],[7,3,2]) expected False: " + str(common_end([1,2,3],[7,3,2])))
print("common_end([1,2,3],[1,3]) expected True: " + str(common_end([1,2,3],[1,3])))


