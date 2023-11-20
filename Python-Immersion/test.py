def att(x,y):
    n = len(x)
    for i in range(n):
        for j in range(i + 1, n):
            print(x[i], y[i], x[j], y[j] )
            if x[i] == y[i] or x[j] == y[j] or abs(x[i] - y[i]) == abs(x[j] - y[j]):      # мое
            # if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):        # от Alex
                print('+2')
            else:
                print('+3')



def check_queens(**data):
    data = data['queens']
    n = len(data)
    x = []
    y = []
    result = []
    for el in data:
        x.append(el[0])
        y.append(el[1])
    print(x,y)
    if n <= 1:
        print('+1')
        return True
    else:
        print(att(x,y))
                
check_queens(queens = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)])