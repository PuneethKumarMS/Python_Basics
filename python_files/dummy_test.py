heights = input('Enter the heights: ').split()

total = 0
count = 0

for h in heights:
    total += int(h)
    count += 1
    
avg = total / count
print("Average Height:", avg)