lst = ['разработка', 'администрирование', 'protocol', 'standard']
i = 0
while i < len(lst):
    lst[i]=lst[i].encode('UTF-8')
    i+=1
print(lst)
i=0
while i < len(lst):
    lst[i]= bytes.decode(lst[i],'UTF-8')
    i+=1
print(lst)