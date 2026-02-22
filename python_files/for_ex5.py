bestSeries = ['Stranger Things',
              'Wednesday',
              'Game of Thrones',
              'Breaking Bad'
              ]

for i in range(3):
    bestSeries.append(bestSeries[i]) # In each iteration it adds the elements to the end

print(len(bestSeries))