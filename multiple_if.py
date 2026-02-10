height = int(input("What is your height ? "))
bill = 0

if height >= 3:
    print("You can ride")
    age = int(input("What is your age ? "))

    if age <= 12:
        bill = 150
        print("Ticket price is 150")

    elif age <= 18:
        bill = 250
        print("Ticket price is 250")

    else:
        bill = 500
        print("Ticket price is 500")
    want_photo = input("Do you want to take photo(Y/N)?")

    if want_photo == 'Y':
        bill = bill + 50
    print(f"Your total bill is {bill}")

else:
    print("Can't ride")
print("Thank you...!!")