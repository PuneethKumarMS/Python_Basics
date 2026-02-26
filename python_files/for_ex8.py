numbers = input('Enter the numbers: ')
num_list = numbers.split()

count = 0
for number in num_list:
    count += 1
print(f"The length of the list is : {count}")

for i in range(count):
     i = int(num_list[i])
print(num_list)

maximum = num_list[0]
for number in num_list:
    if number  > maximum:
        maximum = number
print(f"The maximum number is : {maximum}")



    