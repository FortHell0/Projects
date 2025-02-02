try:
    user_input = int(input("Find Prime Factors. Number: "))
except ValueError:
    print("Enter a valid number!")
    raise SystemExit(0)

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

print(prime_factors(user_input))