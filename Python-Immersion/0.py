num = 0

def to_hex(number):
    hex_digits = "0123456789ABCDEF"
    result = ""
    while number > 0:
        remainder = number % 16
        result = hex_digits[remainder] + result
        number //= 16
    return result


print(f"Шестнадцатеричное представление числа {num}: {to_hex(num)}")

print(hex(num))