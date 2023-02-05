from chardet import detect


# with open('text.txt', encoding='utf-8') as file:
#    for line in file.read():
#        print(line)


def encoding_convert():
    """    Конвертация кодировки в нужную нам, например UTF-8"""
    with open('text.txt',
              'rb') as f_obj:  # открываем объект в формате байтов 'rb'
        content_bytes = f_obj.read()  # type bytes
    detected = detect(content_bytes)  # вернет словарь с колдировками
    print(detected)
    encoding = detected['encoding']  # в словаре находим кодировку
    content_text = content_bytes.decode(encoding)  # декодирем байты в стр

    # перезаписываем файл в нужной нам кодировке
    with open('text.txt', 'w', encoding='utf-8') as f_obj:
        f_obj.write(content_text)


encoding_convert()
