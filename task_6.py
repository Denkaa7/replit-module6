print('Задача 6. Поставьте оценку!')

# Вася выложил своё новое приложение на платформу для начинающих разработчиков,
# на ней пользователи могут ставить оценку приложению от −100 до 100.
# Ему захотелось сравнить количество положительных и отрицательных отзывов,
# для этого он заранее отфильтровал все отзывы так,
# чтобы в конце были те, которые равны нулю.
 
# Напишите программу,
# которая находит количество положительных
# и количество отрицательных чисел в последовательности.
# Последовательность заканчивается на числе 0.
 
# Пример:
# Введите число: −4
# Введите число: −90
# Введите число: 6
# Введите число: 0
# Кол-во положительных чисел: 1
# Кол-во отрицательных чисел: 2


count_p, count_m = 0, 0
num = 1
while num != 0:
  num = int(input('Введите число: '))
  if num > 0:
    count_p += 1
  elif num < 0:
    count_m += 1
  else:
    break
print(f'Количество положительных чисел: {count_p}')   
print(f'Количество отрицательных чисел: {count_m}') 