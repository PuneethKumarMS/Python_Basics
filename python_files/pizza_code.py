pizza = input("Which pizza you want (S/M/L)? : ")
bill = 0
if pizza=="s" or pizza=='s':
    bill = 100
    print("price is 100")

elif pizza=='M' or pizza=='m':
    bill = 200
    print("price is 200")

elif pizza=="L" or pizza=='l':
    bill = 300
    print("price is 300")

pepproni = input("you want pepproni (Y/N):")
if pepproni == 'Y' or pepproni =='y':
    bill = bill + 30

chees = input("You want chees(Y/N): ")
if chees=='Y' or chees == 'y':
    bill = bill + 20
print(f"Your total bill is {bill}")
print("than you..Ejoy..!!")