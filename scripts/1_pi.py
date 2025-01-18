import math

try:
    user_input = int(input("Generate pi up to how many decimals? Enter: "))
except ValueError:
    print("Enter a valid number!")
    raise SystemExit(0)

num = round(math.pi, user_input)

print(num)