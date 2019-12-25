# print(int(str(9009)[::-1]))
biggest=0
for first in range(100,1000):
    for second in range(100,1000):
        result=first*second
        if result == int(str(result)[::-1]):
            if result > biggest:
                biggest = result
#             print(result," - ", first," * ",second)
print(biggest)
