print("Tickt types: ")
budget_class = 500
economy_class = 750
vip_class = 2_000
add_bag_max = 200
add_meal_max = 150

print(f"1. Budget  (500kr) ")
print(f"2. Economy (750kr) ")
print(f"3. VIP     (2_000kr) ")
print(f"\n")

chosen_ticket = 0
chosen_bag = 0
chosen_meal = 0
remove_bag = 0
remove_meal = 0
total_cost = 0

ticket_type = int(input("Input ticket type >> "))

if ticket_type == 1:
    chosen_ticket = 500
elif ticket_type == 2:
    chosen_ticket = 750
else:
    chosen_ticket = 2_000

while True:
    print("\nCurrently you have: ")
    print(f"    ", {chosen_bag}, "bag(s) registered ")
    print(f"    ", {chosen_meal}, "meal(s) registered ")
    print("\n")
    print("Here are your options: ")
    print("1. Add bag (max 1) ")
    print("2. Add meal (max 1) ")
    print("3. Remove bag ")
    print("4. Remove meal ")
    print("5. Finalize ticket ")

    choice = int(input("Your choice >> "))

    if choice == 1:
        if chosen_bag < 1:
            chosen_bag += 1
            total_cost = chosen_ticket + add_bag_max
    elif choice == 2:
        if chosen_meal < 1:
            chosen_meal += 1
            total_cost = chosen_ticket + add_meal_max
    elif choice == 3:
        if chosen_bag >= 1:
            chosen_bag -= 1
            total_cost = chosen_ticket - add_bag_max
    elif choice == 4:
        if chosen_meal >= 1:
            chosen_meal -= 1
            total_cost = chosen_ticket - add_meal_max
    elif choice == 5:

        total_cost = (
            chosen_ticket + (chosen_bag * add_bag_max) + (add_meal_max * chosen_meal)
        )

        print("\nReceipt:")
        print(f"Ticket : {chosen_ticket:>4}kr")

        if chosen_bag:
            print(f"Bag    : {add_bag_max * chosen_bag:>4}kr")
        if chosen_meal:
            print(f"Meal   : {add_meal_max * chosen_meal:>4}kr")
        print("".ljust(8) + "-------")
        print(f"Total  : {total_cost:>4}kr")
        break
