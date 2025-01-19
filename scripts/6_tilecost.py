try:
    width = int(input("Floor Plan Width (meters): "))
except ValueError:
    print("Enter a valid number!")
    raise SystemExit(0)

try:
    height = int(input("Floor Plan Height (meters): "))
except ValueError:
    print("Enter a valid number!")
    raise SystemExit(0)

try:
    cost = int(input("Cost per square meter: "))
except ValueError:
    print("Enter a valid number!")
    raise SystemExit(0)

area = width * height
endcost = area * cost

print(f"It will cost {endcost}.")