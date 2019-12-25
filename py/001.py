###
#https://projecteuler.net/problem=1
###
sum_of_all= 0
for x in range(1000):
    if x%3 == 0:
        sum_of_all+=x
        continue
    if x%5 == 0:
        sum_of_all+=x
print(sum_of_all)
