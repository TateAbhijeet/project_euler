def fibonacci(limit):
    result = []
    a, b = 0, 1
    while a < limit:
        a, b = b, a + b
        result.append(a)
    return result


def fibonacci_generator(limit):
    a, b = 0, 1
    while a < limit:
        a, b = b, a + b
        yield a


def get_primes(count=10, limit=0):
    primes = [2, 3]
    num = 5

    while num <= limit or (not limit and len(primes) < count):
        is_num_prime = True
        
        for prime in primes:
            if prime ** 2 <= num:
                if num % prime == 0:
                    is_num_prime = False
                    break
            else:
                break
                
        if is_num_prime:
            primes.append(num)

        num += 2
    return primes

