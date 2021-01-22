def task_1():
  """1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка."""
  with open ("somefilename", "w") as sfl:
    var = input('Write something')
    while True:
      sfl.write(var+"\n")
      var = input('>')
      if var == "exit":
        break;

def task_2():
  """2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке."""

  with open ("a_file", encoding='utf-8') as a_f:
    lines_counter = 0
    res = {}
    for line in a_f:
      words = line.split(" ")
      qw = len(words)
      res[lines_counter] = qw
      lines_counter += 1
  print(res)

def task_3():
  """3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
  """
  with open("a_file_1", encoding='utf-8') as fo:
    ls = fo.readlines()
    lslp = []
    mid = 0
    for line in ls:
      name, salary = line.split(" ")
      salary = int(salary)
      mid += salary
      if salary < 20000:
        lslp.append(name)
    lslp = ", ".join(lslp)
    print(f"Получают мало: {lslp}")
    print (f"А в среднем люди там получают {mid/len(ls)}")

def task_4():
  """4. Создать (не программно) текстовый файл со следующим содержимым:
  One — 1
  Two — 2
  Three — 3
  Four — 4
  Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
  """

  fo = open("a_file_2", encoding='utf-8')
  usr_engman = False
  dct = ["Адын", "Ддва", "Трры", "Чатыры"]
  dct2 = ""
  for line in fo:
    if not usr_engman:
      num = int((line.split(" "))[2]) - 1
      dct2 += str(dct[num]) + " — " + str(num + 1) + "\n"
  fo.close()
  with open("a_file_2.1", "w", encoding='utf-8') as fo1: 
    fo1.write(dct2)


def task_5():
  """
  5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
  """
  from random import randint
  num_lst = [str(randint(100, 999)) for _ in range(156)]
  f0 = open("num.file", "w")
  f0.write(" ".join(num_lst))
  f0.close()

  f1 = open("num.file")
  fstr = f1.read()
  Arr = fstr.split(" ")
  num_arr = [val for val in map(int, Arr)]
  print(f"Sum of 156 random ints today is {sum(num_arr)}")

def task_6():
  """
  6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
  Примеры строк файла:
  Информатика: 100(л) 50(пр) 20(лаб).
  Физика: 30(л) — 10(лаб)
  Физкультура: — 30(пр) —

  Пример словаря:
  {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
  """

  dct = {}
  with open("a_file_3") as f3:
    for line in f3:
      ar0 = line.replace("\n", "").split(" ")
      ar0[0].removesuffix(":")
      hours = 0      
      for s in ar0[1:]:
        hours += int(s.removesuffix(")")[3:])
      dct[ar0[0]] = hours
  print (dct)


def task_7():
  """
  7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
  Пример строки файла: firm_1 ООО 10000 5000.

  firm_1 ООО 100000 50000
  firm_2 ИП 1560000 500000
  firm_3 ООО 1340000 160000
  firm_4 ИП 2250000 1980000
  firm_5 ИП 2130000 3123000
  firm_6 ООО 1010000 500000

  Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
  Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
  Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
  Итоговый список сохранить в виде json-объекта в соответствующий файл.
  Пример json-объекта:
  [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

  Подсказка: использовать менеджеры контекста."""
  import json 

  average_profit = 0
  firms_dct = {}
  a2json = None
  with open("firms", encoding='utf-8') as fd0:
    counter = 0
    for line in fd0:
      arr = line.split(" ")
      firm, ftype, income, expenses = arr
      income = int(income)
      expenses = int(expenses)
      profit = income - expenses
      firms_dct[firm] = profit
      if profit > 0: 
        average_profit += profit
        counter += 1
    average_profit /= counter
    a2json = [firms_dct, {"average_profit": average_profit}]
  with open("firms_json", "w") as wf0:
    jsonval = json.dump(a2json, wf0)


task_7()
