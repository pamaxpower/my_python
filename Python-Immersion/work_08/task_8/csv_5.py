import csv
with open('biostats.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", \
        "age", ], restkey="new", restval="Main Office", \
        quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(f'{line = }')
        print(f'{line["name"] = }\t{line["age"] = }')

# в параметр fieldname мы передали 3 поле, а в файле у нас 5,
# остальные поля запишутся в новое поле (по значению restkey) 
# в виде списка (не зависимо от кол-ва потерянных поле, 
# хоть 1 хоть 10 - все равно будет список) 