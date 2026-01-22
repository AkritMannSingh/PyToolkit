print("=" * 40)
print("    FRIEND'S KITCHEN ORDER SYSTEM")
print("=" * 40)
print()


print("SELECT YOUR ITEM:")
print("1. Spring Rolls - Rs.39")
print("2. Dosa - Rs.24")
print("3. Dimsons - Rs.49")
print()

choice = input("Enter choice (1/2/3): ")


if choice == "1":
    price = 39
    name = "Spring Rolls"
    
elif choice == "2":
    price = 24
    name = "Dosa"
    
elif choice == "3":
    price = 49
    name = "Dimsons"
    
else:
    price = 0
    name = "Invalid"


if price > 0:
    print()
    print("You selected:", name)
    print("Price: Rs.", price)
    
    print()
    print("SELECT QUANTITY:")
    print("1. One (1)")
    print("2. Two (2)")
    print("3. Three (3)")
    
    qty_choice = input("Enter quantity choice (1/2/3): ")
    
    if qty_choice == "1":
        quantity = 1
    elif qty_choice == "2":
        quantity = 2
    elif qty_choice == "3":
        quantity = 3
    else:
        quantity = 1
        print("Invalid! Defaulting to 1")
    
    total = price * quantity
    
    print()
    print("=" * 30)
    print("BILL SUMMARY:")
    print("-" * 30)
    print("Item:", name)
    print("Quantity:", quantity)
    print("Unit Price: Rs.", price)
    print("Total: Rs.", total)
    print("-" * 30)
    
    
    if total >= 100:
        print("You get 10% discount!")
        discount = total * 10 / 100
        final = total - discount
        print("Discount: Rs.", discount)
        print("Final Total: Rs.", final)
    elif total >= 50:
        print("You get 5% discount!")
        discount = total * 5 / 100
        final = total - discount
        print("Discount: Rs.", discount)
        print("Final Total: Rs.", final)
    else:
        final = total
        print("No discount available")
    
    print("-" * 30)
    
    
    if choice == "1":  
        if quantity == 1:
            time = 5
        elif quantity == 2:
            time = 8
        else:  
            time = 12
    elif choice == "2":  
        if quantity == 1:
            time = 10
        elif quantity == 2:
            time = 15
        else:  
            time = 20
    else: 
        if quantity == 1:
            time = 7
        elif quantity == 2:
            time = 12
        else:  
            time = 17
    
    print("Preparation Time:", time, "minutes")
    print("=" * 30)
    
    print()
    print("RATE YOUR EXPERIENCE:")
    print("1. Excellent")
    print("2. Good")
    print("3. Average")
    print("4. Poor")
    
    rating = input("Enter rating (1/2/3/4): ")
    
    if rating == "1":
        print("Thank you! We're glad you loved it! ")
    elif rating == "2":
        print("Thank you! We're happy you liked it!")
    elif rating == "3":
        print("Thank you! We'll try to improve! ")
    elif rating == "4":
        print("We apologize! We'll do better!")
    else:
        print("Thank you for visiting!")
    
else:
    print("Invalid choice! Please restart.")

print()
print("~" * 40)
print("  Thank you for visiting!")
print("~" * 40)
