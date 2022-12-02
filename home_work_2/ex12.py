

d1 = {'title': 'Samsung Galaxy', 'price': 20000, 'country': 'China', 'year': '2016'}
d2 = {'title': 'Sam Ga', 'price': 500, 'country': 'Russia', 'year': '2020'}

list = [d1, d2]

for k in range(len(list)):
    for key, value in list[k].items():
        print(f"{key} - {value}")