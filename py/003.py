value = 600851475143
cur_value=value
smallest_devisor=2
biggest_prime_factor=2

def find_prime_devisor(value, min_devisor):
    global biggest_prime_factor
    devisor = 0
    for i in range(min_devisor, value//2):
        if value%i == 0:
            #print(i)
            cur_value=value//i
            devisor = i
            if biggest_prime_factor < i:
                biggest_prime_factor=i
            if cur_value>=i:
                find_prime_devisor((cur_value),i)
            return
    # cover case when the value itself is a prime
    if devisor == 0:
        if biggest_prime_factor < value:
            biggest_prime_factor=value
        #print(value)

find_prime_devisor(cur_value,smallest_devisor)
print(biggest_prime_factor)
