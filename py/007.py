sub_result=3
count=10001
primes=[2,3]
while len(primes) < count:
    sub_result += 2
    for k,v in enumerate(primes):
        if sub_result%v == 0:
            break
        if k==len(primes)-1:
            primes.append(sub_result)
print(sub_result)
