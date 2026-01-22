print("Welcome to Character Identifier 🔤")

ch = input("Enter a character: ").strip()


if len(ch) != 1:
    print("Error: Please enter exactly one character.")
else:

    if ch.lower() in 'aeiou':
        print(f"'{ch}' is a vowel.")
    else:
        print(f"'{ch}' is not a vowel.")

print("≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")

print("End of Program..")
