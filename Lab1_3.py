print("Welcome to The Money Bag Transport Calculator (M.B.T.C) ")
print("------------------------------------------------------- ")
print("\n")

truck_size = int(input("Insert the size of the truck (>=L): "))

while truck_size < 100:
    print("Truck size must be no less than 100 (>=L) ")
    truck_size = int(input("Insert the size of the truck (>=L): "))

big_bag = 80
medium_bag = 50
small_bag = 20
total_bag_size = 150
cash_big_bag = 60_000
cash_medium_bag = 30_000
cash_small_bag = 10_000

cal_big_bag = int(truck_size // big_bag)
remainder_space = truck_size % big_bag

cal_medium_bag = int(remainder_space // medium_bag)
remainder_space %= medium_bag

cal_small_bag = int(remainder_space // small_bag)
remainder_space %= small_bag

total_value = (
    (cash_big_bag * cal_big_bag)
    + (cash_medium_bag * cal_medium_bag)
    + (cash_small_bag * cal_small_bag)
)

print(f"Truck size = {truck_size}L:")
print("\n")
print("Parking Plan")
print("------------")
print(f"{cal_big_bag} big bags")
print(f"{cal_medium_bag} medium bags")
print(f"{cal_small_bag} small bags")
print("\n")
print(f"Space left : {remainder_space}L")
print(f"Total value: {total_value}kr")
print("\n")
