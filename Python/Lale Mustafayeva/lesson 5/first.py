def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
        
    
    return True

palindromes = [num for num in range(1, 1001) if is_palindrome(num)]
primes = [num for num in range(1, 1001) if is_prime(num)]

print("Polindromes: ", palindromes, "\n")
print("Primes: ", primes)
