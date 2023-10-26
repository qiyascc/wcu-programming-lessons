def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [i for i in range(300, 400) if i % 10 == 7 and is_prime(i)]

print(numbers)
