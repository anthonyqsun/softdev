def makes10(a, b):
  return a + b == 10 or a == 10 or b == 10

print("makes10(9,10) expected True: " + str(makes10(9,10)))
print("makes10(9,9) expected False: " + str(makes10(9,9)))
print("makes10(1,9) expected True: " + str(makes10(1,9)))


