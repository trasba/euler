forelast_fibo=0
last_fibo=1
cur_fibo=0
all_even=0
while cur_fibo <= 4000000:
    if cur_fibo%2 == 0:
        all_even += cur_fibo
    forelast_fibo = last_fibo
    last_fibo = cur_fibo
    cur_fibo = forelast_fibo + last_fibo
print(all_even)
