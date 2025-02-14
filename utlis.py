def factorial(n):
   if n < 1:   
       return 1
   else:
       return n * factorial(n - 1)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_power_of_5(n):
    if n < 1:
        return False
    while n % 5 == 0:
        n //= 5
    return n == 1

def is_power_of_2(n):
    if n < 1:
        return False
    return (n & (n - 1)) == 0


