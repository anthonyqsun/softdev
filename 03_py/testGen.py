# print("sleep_in(False, False) expected True: " + sleep_in(False,False))
while True:
    s=""
    fx =     input("fx    : ")
    for x in range(3):
        params = input("params: ")
        val =    input("val   : ")
        s+= "print(\"{}({}) expected {}: \" + str({}({})))\n".format(fx,params,val,fx,params)
    print(s)
