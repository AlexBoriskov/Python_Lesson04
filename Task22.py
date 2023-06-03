# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

def ExaminationType(number):
    while type(number) != int:
        try:
            number = int(number)
        except ValueError:
            print ("Ошибка. Введено не число!")
            number = input("Введи повторно: ")
    return number

n = input("Введите размер списка №1: ")
n = ExaminationType(n)

m = input("Введите размер списка №2: ")
m = ExaminationType(m)

spisok01 = [randint(0,30) for i in range(n)]
spisok02 = [randint(0,50) for i in range(m)]

print ("Список №1: {0} \n" .format(spisok01))
print ("Список №2: {0} \n" .format(spisok02))

copy_spisok01 = set(spisok01)
copy_spisok01 &= frozenset(spisok02)
print (copy_spisok01)
