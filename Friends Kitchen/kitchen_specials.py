print("✩" * 40)
print("       FRIEND'S KITCHEN DAILY SPECIAL")
print("✩" * 40)
print()


print("TODAY'S SPECIAL: Buy 2, Get 10% off!")
print()


print("MENU CARD:")
print("-" * 35)
print("CODE  ITEM            PRICE")
print("-" * 35)
print("  1   Spring Rolls    Rs. 39")
print("  2   Dosa            Rs. 24")
print("  3   Dimsons         Rs. 49")
print("-" * 35)
print()


user_choice = input("Enter item code (1/2/3): ")


if user_choice == "1":
    item = "Spring Rolls"
    cost = 39
    
    print()
    print("You chose: Spring Rolls")
    print("Price: Rs. 39 per plate (2 pieces)")
    
elif user_choice == "2":
    item = "Dosa"
    cost = 24
    
    print()
    print("You chose: Dosa")
    print("Price: Rs. 24 per plate (10 pieces)")
    
elif user_choice == "3":
    item = "Dimsons"
    cost = 49
    
    print()
    print("You chose: Dimsons")
    print("Price: Rs. 49 per plate (12 pieces)")
    
else:
    item = "Nothing"
    cost = 0
    print("Wrong choice! Please try again.")


if cost > 0:
    print()
    print("How many plates?")
    print("1. One Plate")
    print("2. Two Plates (TODAY'S SPECIAL)")
    print("3. Three Plates")
    
    plates = input("Enter 1, 2 or 3: ")
    
    
    if plates == "1":
        plates_num = 1
        amount = cost * 1
        special = "No"
        
    elif plates == "2":
        plates_num = 2
        
        amount = cost * 2
        discount = amount * 10 / 100
        amount = amount - discount
        special = "Yes"
        
    elif plates == "3":
        plates_num = 3
        amount = cost * 3
        special = "No"
        
    else:
        plates_num = 1
        amount = cost * 1
        special = "No"
        print("Invalid! Ordering 1 plate.")
    
    
    print()
    print("»" * 40)
    print("             YOUR ORDER")
    print("»" * 40)
    print("Item:", item)
    print("Plates:", plates_num)
    
    if special == "Yes":
        print("TODAY'S SPECIAL: Applied! ✓")
        print("(10% discount on 2 plates)")
    
    print("Amount to pay: Rs.", amount)
    print("»" * 40)
    
    
    print()
    print("Need something extra?")
    print("1. Extra Sauce (Rs. 5)")
    print("2. Extra Spicy (Rs. 10)")
    print("3. No, thanks")
    
    extra = input("Choose (1/2/3): ")
    
    if extra == "1":
        amount = amount + 5
        print("Added: Extra Sauce (+Rs. 5)")
    elif extra == "2":
        amount = amount + 10
        print("Added: Extra Spicy (+Rs. 10)")
    else:
        print("No extras added.")
    
    print()
    print("Final Amount: Rs.", amount)
    print()
    print("Order will be ready in 15 minutes!")
    print("Thank you!")

print()
print("=" * 40)
print("   Visit us again at Friend's Kitchen!")
print("=" * 40)