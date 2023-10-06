# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств
from random import randint

n = int(input("Введите количество элементов списка N ", ))
m = int(input("Введите количество элементов списка M ", ))

list1 = []
for i in range(n):
    list1.append(randint(0, 20))

list1.sort()  
print("Список N", list1)

list2 = []
for i in range(m):
    list2.append(randint(0, 20))

list2.sort()
print("Список M", list2)

list3 = list(set(list1 + list2))
print(list3)