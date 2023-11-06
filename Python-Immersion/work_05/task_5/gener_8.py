'''
Проверка
'''
data = {2, 4, 4, 6, 8, 10, 12}

res1 = {None: item for item in data if item > 4}
res2 = (item for item in data if item > 4)
res3 = [[item] for item in data if item > 4]

# -) res1 = {None}
# +) res2 = generator object at ...
# +) res3 = [[6],[8],[10],[12]]

print(res1, res2, res3, sep='\n')
