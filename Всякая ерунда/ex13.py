def is_password_good(txt):
    flag = False
    if len(txt) >= 8:
        flag = True
        for i in range(len(txt)):
            print(txt[i])
            if txt[i].isupper() == True:
                flag = True
            if txt[i].islower() == True:
                flag = True
            if txt[i].isdigit() == True:
                flag = True
            else:
                flag = False
    print(flag)

# считываем данные
password = 'aaA1aaaa'

# вызываем функцию
print(is_password_good(password))