"""
Требуется определить является ли год весокосным, то выведите Yes или No
если его номер кратен 4 но не кратен 100, или кратен 400

2016

Yes
"""

year = int(input('введите год '))
if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
    print ('Yes')
else:
    print ('No')