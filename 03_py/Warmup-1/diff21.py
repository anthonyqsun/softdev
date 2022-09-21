def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return 2*(n-21)

print("diff21(19) expected 2: " + str(diff21(19)))
print("diff21(22) expected 2: " + str(diff21(22)))
print("diff21(-1) expected 22: " + str(diff21(-1)))
