prime_number =1
prime_count = 0
divisor_count = 0
while True:
    prime_number = prime_number +1
    divisor_count = 0
    for i in range(1, prime_number+1):
        if prime_number % i == 0:
            divisor_count = divisor_count +1
    if divisor_count == 2:
        print prime_number,
        prime_count = prime_count +1
        if prime_count % 10 == 0:
                print ''
    if prime_count == 50:
            break
