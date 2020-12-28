from random import randint
from functools import reduce
from itertools import count, islice, cycle


def task_2():
  """
  2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
  Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
  Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
  Результат: [12, 44, 4, 10, 78, 123].
  """
  var_list = [randint(0, 1000) for _ in range(11)]

  def l_generator():
    for i, v in enumerate(var_list):
      if i > 0:
        if v > var_list[i-1]:
          yield v

  g = l_generator()

  ret_list = [v for v in g]

  print (var_list)
  print (ret_list)
##############################################

def task_3():
  """
  3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
  Подсказка: использовать функцию range() и генератор.
  """
  lst = [val for val in range (20, 241) if val % 20 == 0 or val % 21 == 0]
  print (lst)


def task_4():
  """
  4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
  Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
  Результат: [23, 1, 3, 10, 4, 11]
  """
  lst1 = [randint(10, 33) for _ in range (55)]
  dct1 = {}
  res = []

  def clear_list_generator ():
    for val in lst1:
      count = dct1.setdefault(val, 0)
      if count == 0: 
        yield val
      dct1[val] += 1

  g = clear_list_generator()
  res = [val for val in g]

  print(lst1, res)


def task_5():
  """
  5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
  """
  lst_evens = [val for val in range(100, 1001) if val % 2 == 0]
  le_sum = reduce(lambda x, y: x + y, lst_evens)

  # print(lst_evens)
  print(le_sum)

def task_6():
  """
  6. Реализовать два небольших скрипта:
  а) итератор, генерирующий целые числа, начиная с указанного,
  б) итератор, повторяющий элементы некоторого списка, определенного заранее.
  Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
  Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
  """
  start = 156
  quantity = 13
  lst = [val for val in islice(count(start), quantity)]
  print (lst)
  print()

  lst1 = [randint(0, 156) for _ in range(11)]
  lst2 = [val for val in islice(cycle(lst1), len(lst1) * 3)]
  print (lst1)
  print()
  print (lst2)
    

def task_7():
  """
  7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
  Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
  """
  def factorial_generator(limit):
    if limit > 10:
      raise ValueError
    step_counter = 0
    prev = 1
    while True:
      step_counter += 1
      prev *= step_counter
      yield (step_counter, prev)
      if step_counter == limit:
        raise StopIteration
  
  limit = 5
  fg = factorial_generator(limit)
  for i in range(limit):
    print (next(fg))

task_2()
task_3()
task_4()
task_5()
task_6()
task_7()
