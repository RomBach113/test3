# Задайте список. 
# Напишите программу, которая определит, 
# присутствует ли в заданном 
# списке строк некое число.

spisok = (1,2,5,3,22,4,23,44,1,23,45,76,7)
print(spisok)

def sp (a):
    s = int(input('введите искомое число: '))
    if s in a:
        print('такое число есть')
    else:
        print('такого числа нет')

sp(spisok)