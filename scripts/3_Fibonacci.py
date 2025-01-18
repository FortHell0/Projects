try:
    user_input = int(input("Generate Fibonacci sequence to Nth number OR up to a certain number? Type '1' for Nth number and '2' for a set number: "))
except ValueError:
    print("Enter a valid number!")
    raise SystemExit(0)

prev = [0, 1]
num = 0

if user_input == 1:
    try:
        user_input = int(input("Generate Fibonacci sequence to Nth number. Number: "))
    except ValueError:
        print("Enter a valid number!")
        raise SystemExit(0)
    
    print(f"{prev[0]}\n{prev[1]}")

    for x in range(user_input):
        num = prev[0] + prev[1]
        prev[0] = prev[1]
        prev[1] = num

        print(num)

if user_input == 2:
    try:
        user_input = int(input("Generate Fibonacci sequence up to a number. Number: "))
    except ValueError:
        print("Enter a valid number!")
        raise SystemExit(0)
    
    print(f"{prev[0]}\n{prev[1]}")
    
    while num < user_input:
        num = prev[0] + prev[1]
        prev[0] = prev[1]
        prev[1] = num

        print(num)