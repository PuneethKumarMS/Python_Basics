characters = ['Eleven', 'Steve', 'Dustin', 'Will', 'Max', 'Lucas', 'Vecna']

survivors = []

for c in characters:
    if 's' in c.lower():
        survivors.append(c)

print(survivors)