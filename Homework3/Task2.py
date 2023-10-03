# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены
# только по окружности. Таким образом, у каждого куста
# есть ровно два соседних. Всего на грядке растет N кустов.

# Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло
# различное число ягод – на i-ом кусте выросло ai ягод.

# В этом фермерском хозяйстве внедрена система
# автоматического сбора черники. Эта система
# состоит из управляющего модуля и нескольких
# собирающих модулей. Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального
# числа ягод, которое может собрать за один заход
# собирающий модуль, находясь перед некоторым
# кустом заданной во входном файле грядки.

n = int(input("Введите число высаженных кустов на грядке ", ))

bush_sum = 0

import random

for i in range(0, n-1, 3): 
	bush_sum += random.randint(0,15) #Задается рандомное число ягод на трех кустах и складывается в общую сумму
	
print(bush_sum)