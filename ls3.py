""" 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль. """

def divide (arg0, arg1):
  ret = -1
  if arg1 == 0:
    print("Cannot divide by zero")
  else:
    ret = arg0 / arg1
  return ret

  vars = []
  for i in range (0, 2):
    vars.append(input (f'Need arg{i}'))
  print(f"Division gives {divide(vars[0], vars[1])}")

""" 
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""

questions = [
  "Your name?",
  "Your surname?"
  "Your age?",
  "Your city?"
  "Your email?"
  "Your phone number?"
]
answers = []

for q in questions:
  answers.append(input(q))

def format_string(name, surname, age, city, email, phone_num)
  print (f"""{name} {surname}, {age} years old, living in {city} may be reached by email {email} or phone at {phone_num}""")

format_string(answers[0], answers[1], answers[2], answers[3], answers[4], answers[5])

"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""
def my_func (a0, a1, a2):
  m0 = max(a0, a1)
  m1 = max(a1, a2)
  return m0 + m1

"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

def my_func0 (pos, neg):
  if neg > 0:
    neg *= -1
  res = 1
  for i in range (0, abs(neg)):
    res *= pos
  return 1 / res

def my_func1 (pos, neg):
  return pos ** neg

print(my_func0(2, -2) == my_func1(2, -2))

"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

total = 0
flag_exit = False
while True:
  nums = input("Give a list of ints, separated by spaces, upon finishing, press enter or write 'q' + enter to exit: ").split(" ")
  if nums[-1] == 'q':
    flag_exit = True

  ulist = []
  for val in nums:
    if not val.isdigit():
      if not flag_exit:
        print (f"'{val}' is NaN, dropped")
    else:
      ulist.append(int(val))

  total += sum(ulist)
  print(f"Now total is {total}")
  if flag_exit:
    break

"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func()
"""
def int_func(lineofletters):
  #although its role has nothing to do with ints )
  return lineofletters.capitalize()

def my_func():
  str_arr = input("Your line of latin words, separated by one space: ").split(" ")
  ret_arr = []
  for s in str_arr:
    ret_arr.append(int_func(s))
  print(" ".join(ret_arr))

my_func()

def better_my_func():
  str_l = input("Your line of latin words, separated by one space: ")
  return str_l.title()

print(better_my_func())
