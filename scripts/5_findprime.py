import sympy

num = 1

while True:
    user_input = input("Do you want the next prime number? Response: ")

    if str.lower(user_input) == "yes" or str.lower(user_input) == "y":
        num += 1

        while True:
            if sympy.isprime(num):
                print(num)
                break
            else:
                num += 1
    else:
        raise SystemExit(0)