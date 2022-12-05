from itertools import cycle

progr_lang = ["python", "java", "perl", "javascript"]
iter = cycle(progr_lang)
print(type(iter))

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(round(1.4365436, 2))

"""
python
java
perl
javascript
python
java
"""
