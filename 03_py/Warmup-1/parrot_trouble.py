def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)
    
print("parrot_trouble(True,6) expected True: " + str(parrot_trouble(True,6)))
print("parrot_trouble(True,7) expected False: " + str(parrot_trouble(True,7)))
print("parrot_trouble(False,6) expected False: " + str(parrot_trouble(False,6)))


