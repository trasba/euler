sum_of_range=0
sum_of_square_of_range = 0

for i in range(1,100+1):
    sum_of_range+=i
    sum_of_square_of_range+=pow(i,2)
print(pow(sum_of_range,2)-sum_of_square_of_range)
