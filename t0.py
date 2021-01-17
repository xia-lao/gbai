""" 
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

work_hours, money_per_hour, bonus = argv[1:4]
try:
  iwork_hours = int(work_hours)
  imoney_per_hour = int(money_per_hour)
  ibonus = int(bonus)
except ValueError:
  print("Bad parameters format: expected integers")

print(iwork_hours * imoney_per_hour + ibonus)
