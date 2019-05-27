# Задание 1.1

value = int(input("Введите максимальное целое положительное число \t" ))

def fibb(el):
  """Вычисление ряда чисел Фибоначчи рекурсией. 
      Вызов функции самой себя
  """
  if el > 1:
    return fibb(el-1) + fibb(el-2)
  return el
for i in range(value):
  print(i, "=", fibb(i))
  
#ответ при value = 10:
# 0 = 0
# 1 = 1
# 2 = 1
# 3 = 2
# 4 = 3
# 5 = 5
# 6 = 8
# 7 = 13
# 8 = 21
# 9 = 34

  
# Задание 1.2

value = int(input("Введите максимальное целое положительное число \t" ))

def fib():
"""
Итератор - генератор
"""
    a, b = 0, 1
    while True:            # Первая итерация
      yield a              # yield 0 => начинаем с нуля
      a, b = b, a + b      # a теперь = 1, b будет также 1, (0 + 1)
    
for index, fibonacci_number in zip(range(value), fib()):
    print('{i}: {f}'.format(i=index, f=fibonacci_number))
    
# ответ при value = 10:
# 0: 0
# 1: 1
# 2: 1
# 3: 2
# 4: 3
# 5: 5
# 6: 8
# 7: 13
# 8: 21
# 9: 34
