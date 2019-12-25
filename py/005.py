#high load on cpu expected
check = True
highest_divisor=20
test=highest_divisor
while check:
    test+=1
    for i in reversed(range(2,highest_divisor+1)):
        #print(i)
        if test%i!=0:
            break
        if i == 2:            
            print("gotcha ",test)
            check = False
            break

#232792560
