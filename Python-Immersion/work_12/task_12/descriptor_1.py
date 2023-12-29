'''
Дескриптор - атрибут объекта со "связанным поведением", 
те такой атрибут, при доступе к которому его поведение 
переопределяется методом протокола дескриптора
Это методы __get__, __set__, __delete__.
Если один из этих методов определен в объекте, то можно сказать что это метод дескриптор

'''

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


