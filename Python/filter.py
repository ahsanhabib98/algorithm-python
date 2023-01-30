counts = {2:4, 3:3, 5:0, 7:1, 11:0}
counts = dict(filter(lambda item: item[1]!=0, counts.items()))
print(counts)
