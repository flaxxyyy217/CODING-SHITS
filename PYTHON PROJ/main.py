
user_money = float(input("Enter your current cash: PhP "))
choice = None


menu = {
        1: ("Fries: PhP 120"),
        2: ("Burher: PhP 45"),
        3: ("drinks: PhP 28"),
        4: ("Pizza: PhP 150"),
        5: ("Pasta: PhP 100"),
        6: ("Salad: PhP 80"),
        7: ("Ice Cream: PhP 60"),
        8: ("Sundae: PhP 70"),
        9: ("Milkshake: PhP 90"),
        10: ("Coffee: PhP 50"),
        11: ("Tea: PhP 40"),}

if user_money <= 0:
    print("You don't have enough money to buy anything.")
elif user_money > 1000000:
    print("You can buy the whole stock!!.")
else:
    print("You can buy anything from the menu.")

while user_money >0 and choice != 0:
    print("\nMenu:")
    for item in menu:
        print(f"{item}. {menu[item]}")
    
    choice = input("\nWhat would you like to buy? (Type 0 to leave): ")
    

    def get_price(choice):
        prices = {
            1: 120,
            2: 45,
            3: 28,
            4: 150,
            5: 100,
            6: 80,
            7: 60,
            8: 70,
            9: 90,
            10: 50,
            11: 40
        }
        return prices.get(choice, None)
    while True:
        if choice < int(0) or choice > int(11):
            print("Invalid input. Please enter a number corresponding to the menu item.")
            continue
        #WHAT THE FUCK IS WRONG WITH THIS!!!
        else:
            choice = int(choice)
            if choice in menu:
                item_price = get_price(choice)
                if user_money >= item_price:
                    user_money -= item_price
                    print(f"You bought {menu[choice]} and your remaining cash is: PhP {user_money:.2f}")
                    question = input("Are you sure you want to buy this item? (y/n): ").lower()
                    if question == 'y':
                        print(f"You have successfully purchased {menu[choice]}.")
                        continue
                    elif question == 'n':
                        user_money += item_price
                        print(f"Purchase canceled. Your remaining cash is: PhP {user_money:.2f}")
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
                        continue
                else:
                    print("You don't have enough money to buy this item.")
                e
            else:
                print("Invalid choice. Please select a valid item from the menu.")
        
        
