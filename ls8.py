"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию (проверку на корректность) числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
class Date:
  date = []

  def __init__(self, str_date):
    """
    date is to be passed, separated by "-"
    """
    self.str_date = str_date
    self.parse(str_date)
    Date.validate(self.date)

  @classmethod
  def parse(self, str_date):
    try:
      self.date = [val for val in map(int, str_date.split("-"))]
      print (self.date)
    except Exception:
      print(f"Need integer values for date in {str_date}")

  @staticmethod
  def validate(array_date):
    ad = array_date
    if 1 > ad[0] or ad[0] > 31:
      raise Exception("Invalid integer passed for day of month")
    if 1 > ad[1] or ad[1] > 12:
      raise Exception("Invalid integer passed for month")
    if 1900 > ad[2] or ad[2] > 2100:
      raise Exception("Invalid integer passed for year")

  def __str__(self):
    ret = "The date is "
    parts = []
    for val in self.date:
      parts.append(str(val))
      if val < 10:
        parts[-1] = "0" + parts[-1]        
    ret += "-".join(parts)
    return ret

def date_test():
  try:
    d = Date("10-s4-1904") #with error
  except Exception as e:
    print (e)
  finally:
    print ("\tWe go on to next error")

  try:
    d = Date("33-13-2101") #with error
  except Exception as e:
    print (e)
  finally:
    print("\tNow we proceed to normal execution")

  d = Date("10-04-1904")
  print(d)  

"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class ZeroDivErr(Exception):
  def __init__(self, msg):
    self.message = msg

def exc_test():  
  try:
    divizor = input("We divide 5 by: ")
    if divizor == 0:
      raise ZeroDivErr
  except ZeroDivErr:
    print ("Your divizor is 0")
  print ("Execution goes on")

"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""
class BadInputException(Exception):
  def __init__(self, message):
    self.message = message

def bie_test():
  aDataSet = []
  while True:
    data = input("Please, write new member (it should be integer value): ")
    
    if data == "stop":
      break

    try:
      if not data.isnumeric():
        raise BadInputException("I said INTEGER VALUE!")
      else:
        aDataSet.append(int(data))
    except BadInputException as bie:
      print (bie)
      print("Retry...")
  print (f"Total collected data is: \n {aDataSet}")

"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""
class OfficeEquipment():
  def __init__(self):
    self.on_balance_of = "WareHouse"
  
  def price(self): pass
  def ID(self): pass

  def __eq__(self, other):
    if self.ID == other.ID:
      return True
    return False


class OEPrinter(OfficeEquipment):
  __ID = -1

  def __init__(self, manufacturer, model, price):
    self.__name = f"{manufacturer} {model}"
    self.__price = price

  @property
  def price(self):
    return self.__price

  @property
  def ID(self):
    return self.__ID
  @ID.setter
  def ID(self, ID):
    if self.__ID == -1:
      self.__ID = ID
    else:
      raise Exception("Cannot change already set ID")

  @property
  def name(self):
    return self.__name

  def __str__(self):
    return f"Printer '{self.__name}': ${self.price}, ID#{self.ID}"

class OEScanner(OfficeEquipment):
  __ID = -1

  def __init__(self, manufacturer, model, price):
    self.__name = f"{manufacturer} {model}"
    self.__price = price

  @property
  def price(self):
    return self.__price
  @price.setter

  @property
  def ID(self):
    return self.__ID
  @ID.setter
  def ID(self, ID):
    if self.__ID == -1:
      self.__ID = ID
    else:
      raise Exception("Cannot change already set ID")

  @property
  def name(self):
    return self.__name

  def __str__(self):
    return f"Scanner '{self.__name}': ${self.price * 1.31}, ID#{self.ID}"

class OECopier(OfficeEquipment):
  __ID = -1

  def __init__(self, manufacturer, model, price):
    self.__name = f"{manufacturer} {model}"
    self.__price = price

  @property
  def price(self):
    return self.__price

  @property
  def ID(self):
    return self.__ID
  @ID.setter
  def ID(self, ID):
    if self.__ID == -1:
      self.__ID = ID
    else:
      raise Exception("Cannot change already set ID")

  @property
  def name(self):
    return self.__name

  def __str__(self):
    return f"Copier '{self.__name}': ${self.price}, ID#{self.ID}"

"""
5. Продолжить работу над прошлым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
"""
import json
import copy

class OEWareHouse:

  def __init__(self):
    
    Storage = {
      'Types': ['OEPrinter', 'OEScanner', 'OECopier'],
      'Departments': ['Billing', 'Debilling', 'Rebilling'],
      'IDs': [],
      "Balance": 0, 
      'Qty': 0, 
      "Away": 0, 
      'ByName': {},
      'ByType': {val: [] for val in self.Storage['Types']},
      'LastID': 0
    }
    # self.Storage['ByType'] = 

  def _save(self):
    with open("current_warehouse.db", "w") as ff:
      json.dump((self.IDs, self.Storage, self.LastID), ff)

  def add(self, equip):
    s = self.Storage
    equip.ID = s['LastID'] #after previous addition the id was incremented, never decremented, give this new number to the equipment unit
    try:
      s['ByName'][equip.name].append(equip.ID) #add new equipment to the existing list 
    except KeyError: #if no such list
      s['ByName'][equip.name] = [] #if the equopment is of new kind, create new list for such models
      s['ByName'][equip.name].append(equip.ID) #and retry addition to the existing list
    finally:
      s['IDs'].append(equip.ID) #add newly given id to a list of existing ids
      s['Balance'] += equip.price #warehouse raises in financial responsibility
      s['Qty'] += 1 #increase total units quantity

      s[type(equip).__name__].append(equip.ID) #add id of an equipment to the list of equipment by types
      s[equip.ID] = equip #add an object of corresponding type to the general storage
      s['LastID'] += 1 #ids never go down, so just increment used id numbers

  def discard(self, equip):
    s = self.Storage
    if equip.ID in s['IDs']:
      s['IDs'].remove(equip.ID)
      s['ByName'][equip.name].remove(equip.ID)
      del s[equip.ID]
      s['Balance'] -= equip.price

  def find_available_by_name(self, manuf, model):
    s = self.Storage
    name = f"{manuf} {model}"
    if name in s['ByName'] and len(s['ByName']) > 0:
      return s['ByName'][name][-1]

  def give_to(self, ob_type, dept):
    s = self.Storage
    retobj = Null
    if 0 < dept < len(s['Departments']): #if no mistake in dept index 
      if 0 < ob_type < len(s['Types']): #and no mistake in type of equipment
        ot = s['Types'][ob_type] #get type name
        if len(s[s['Types'][ob_type]]) > 0: #if there are models of the type
          retobj = s[s['Types'][ob_type]][-1] #get the last one from the list
          retobj.on_balance_of = s['Departments'][dept]
          del s[s['Types'][ob_type]][-1]
          s['Away'] += 1

"""
6. Продолжить работу над заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, нельзя отправить принтеры в виде строки или меньше 0.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""

def task_6():
  print ("""
  Если требовалось сделать задание целиком, то я не успел ((. А сдать что-то хоть готовое хочется. Буду доделывать постепенно. Продумать всю логику подобной системы учёта довольно непросто оказалось, размах части идей я уже выбросил в файл ls8_tmp_ideas.py
  """)

"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""

class MyComplex:
  Re = 0
  Im = 0

  def __init__(self, re, im):
      self.Re = re
      self.Im = im
  
  def __add__(self, other):
    return MyComplex(self.Re + other.Re, self.Im + other.Im)

  def __mul__(self, other):
    #ac-bd, ad+bc
    return MyComplex((self.Re * other.Re - self.Im * other.Im), 
                     (self.Re * other.Im + self.Im * other.Re))

  def __str__(self):
    sre = ""
    sim = "+"
    if self.Re < 0:
      sre = "-"
    if self.Im < 0:
      sim = "-"
    return f"({sre}{abs(self.Re)}{sim}{abs(self.Im)}j)"

def mycomp_test():
  c0 = complex(3, 4)
  c1 = complex(5, 6)
  print(c0 + c1)
  print(c0 * c1)

  m0 = MyComplex(3, 4)
  m1 = MyComplex(5, 6)

  print(m0 + m1)
  print(m0 * m1)

def run()
  bie_test()
  exc_test()
  date_test()
  mycomp_test()

run()
