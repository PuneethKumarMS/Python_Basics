movies = ["Inception", "Interstellar", "Batman"]
log = {}

for m in movies:
    log[m] = log.get(m, 0) + 1
    m = "Avatar"

print(log)