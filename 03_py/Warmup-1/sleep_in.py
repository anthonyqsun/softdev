def sleep_in(weekday, vacation):
  return not weekday or vacation

print("sleep_in(False,False) expected True: " + str(sleep_in(False,False)))
print("sleep_in(True,False) expected False: " + str(sleep_in(True,False)))
print("sleep_in(False,True) expected True: " + str(sleep_in(False,True)))

