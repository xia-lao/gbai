# coding=utf-8
"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""
class Matrix:

  def __init__(self, args):
    # consider matrix to be only 2-dim and only square
    if len(args) != len(args[0]):
      print (args)
      raise Exception("Need only square matrix!")
    # length of matrix is by length of first member
    self.length = len(args)
    self.matrix = args

  def __str__(self):
    return str(self.matrix)

  def __add__(self, matrix2):
    if matrix2.length != self.length:
      raise Exception("Can agg only equal length matrices")
    return Matrix([[self.matrix[i][j] + matrix2.matrix[i][j] for i in range(self.length)] for j in range(self.length)])

"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod
class Clothes(ABC):
  @abstractmethod
  def consume(self):
    pass

class Coat(Clothes):
  def __init__(self, V=1):
    self.__V = V

  def __str__(self):
    return f"{self.consume()} is consumed for coat"

  def consume(self):
    return self.V/6.5 + 0.5

  @property
  def V(self):
    return self.__V
  
  @V.setter
  def V(self, num):
    self.__V = num

class Suit(Clothes):
  def __init__(self, H=1):
    self.__H = H

  def __str__(self):
    return f"{self.consume()} is consumed for suit"
  
  def consume(self):
    return 2 * self.__H + 0.3

  @property
  def H(self):
    return self.__H
  
  @H.setter
  def H(self, num):
    self.__H = num


"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
"""
from math import ceil

class Cell():
  def __init__(self, quantity):
    self.quantity = quantity

  @property
  def quantity(self):
    return self.__q

  @quantity.setter
  def quantity(self, quantity):
    if type(quantity) != int:
      quantity = ceil(quantity)
    self.__q = quantity

  def __add__(self, other):
    return Cell(self.quantity * other.quantity)

  def __sub__(self, other):
    q = self.quantity - other.quantity
    if q <= 0:
      raise Exception("Cannot substract greater from lesser cells")
    else:
      return Cell()

  def __mul__(self, other):
    return Cell(self.quantity * other.quantity)

  def __truediv__(self, other):
    return Cell(ceil(self.quantity / other.quantity))

  def __str__(self):
    return '*' * self.quantity
  
  """
  В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
  Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
  Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
  Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
  Подсказка: подробный список операторов для перегрузки доступен по ссылке.
  """
  def make_order(self, num_in_row):
    ret = str(self)
    if num_in_row < self.quantity:
      ret = ""
      cnt = self.quantity // num_in_row #full
      end = self.quantity - (cnt * num_in_row) #end
      for i in range(cnt):
        ret += '*' * num_in_row + "\n"
      if end != 0:
        ret += '*' * end
      else:
        ret = ret.strip("\n")
    return ret


def run():
  def matrix_test():
    a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    c = a + b
    print(c)

  def clothes_test():
    # c0 = Clothes() #raises as should
    print(Coat(2))
    print(Suit(2))

  def cell_test():
    cc = Cell(24)
    print("\n\t1:\n", cc.make_order(6))
    c0 = Cell(10)
    c1 = Cell(13)
    # c2 = c0 - c1 #raises as should
    c3 = c0 + c1
    c4 = c0 * c1
    c5 = c0 / c1

    print("\n\t2:\n", c3.make_order(6))
    print("\n\t3:\n", c4.make_order(6))
    print("\n\t4:\n", c5.make_order(6))

  
  # matrix_test()
  # clothes_test()
  cell_test()

run()
