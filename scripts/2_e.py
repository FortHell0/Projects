import math

try:
    user_input = int(input("Generate e up to how many decimals? Enter: "))
except ValueError:
    print("Enter a valid number!")
    raise SystemExit(0)

num = round(math.e, user_input)

print(num)