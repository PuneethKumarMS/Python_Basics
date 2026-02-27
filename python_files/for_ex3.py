numbers = [1, 2, 4, 11, -2, 85]

for i in numbers:
    if i % 6  == 0:
        print(i)    
        break
else:
    print("There is no number divisible by 6") # this block would be executed only after the completion of for_loop
