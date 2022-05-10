print('Задача 10. Игра «Компьютер угадывает число»')

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.
 
# Напишите программу, 
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.
 
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.


input('Загадайте число между 1 и 100 (включительно) и нажмите на ENTER.')
count, flag, down = 0, 0, 0
up = 100

while flag != 1:
  count += 1
  midle = int((up + down) / 2)
  #print(midle)
  flag = int(input(f'\nТвое число равно, меньше или больше, чем число {midle}?\nВведи:\n1 — если равно\n2 — если больше\n3 — eсли меньше\n'))
  if flag == 2:
    down = midle
  elif flag == 3:
    up = midle
print(f'Я угадал твоё число {midle} за {count} итераций.') 