import random
name = input("Enter the names separated by comma: ")
name_split = name.split(",")
length = len(name_split)
choices = random.randint(0,length-1)
print(name_split)
print(f"{name_split[choices]} will pay the bill")

       #or

'''import random
name = input("Enter the names separated by comma: ")
name_split = name.split(",")
print(name_split)
choice = random.choice(name_split)
print(f"{choice} will pay the bill")'''

      #or

'''import random
name = ['Puneeth','Nithish','Shridhar','Abhishek','Shashidhar']
print(name)
choice = random.choice(name)
print(f"{choice} will pay the bill")'''



