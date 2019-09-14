def largest_prime_factor(num):
    factors = []
    i = 2
    while i * i <= num:
        if num % i:
            i = i + 1    
        else:
            num = num // i
            factors.append(i)
    
    if num > 1:
        factors.append(num)
            
    return factors


print(largest_prime_factor(600851475143))


n = 16
i = 2
while i * i < n:
     while n % i == 0:
         n = n / i
     i = i + 1

# print (n)
