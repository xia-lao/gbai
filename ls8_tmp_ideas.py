from abc import ABC, abstractmethod

class TooBigAUnitException(Exception):
  def __init__(self, message="You surpass the volume of the warehouse"):
    self.message = message

class OfficeEquipment(ABC):
  @abstractmethod
  def price(self): pass

  @abstractmethod
  def ID(self): pass

  @abstractmethod
  def product_name(self): pass

  @abstractmethod
  def volume(self): pass

  @abstractmethod
  def max_paper_size(self): pass

class OEPrinter(OfficeEquipment):
  __ID = -1

  def __init__(self, manufacturer, model, price, box_volume, max_paper_size="A4"):
    self.__name = f"{manufacturer} {model}"
    self.__price = price
    self.__volume = box_volume
    self.__max_paper_size = max_paper_size

  @property
  def volume(self): #readonly
    return self.__volume

  @property
  def price(self):
    return self.__price
  @price.setter
  def price(self, sum):
    self.__price = sum

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
    return f"Printer '{self.__name}', sold at min. ${self.price * 1.31}, ID#{self.ID}, uses {self.volume} of space"

  @property
  def max_paper_size(self):
    return self.__max_paper_size

class OEScanner(OfficeEquipment):
  __ID = -1

  def __init__(self, manufacturer, model, price, box_volume, max_paper_size="A4", both_sides=False):
    self.__name = f"{manufacturer} {model}"
    self.__price = price
    self.__volume = box_volume
    self.__max_paper_size = max_paper_size
    self.__both_sides = both_sides
    self.__lamp_type = []

  @property
  def both_sides(self):
    return self.__both_sides

  def possible_types_of_lamps(self, lamp_type):
    print("Please, write down the types of lamps for the scanner\nNo matter what bullshit you write")
    while True:
      self.__lamp_type.append(input(f"Please, write lamp type for the {self.name}: "))

  @property
  def volume(self): #readonly
    return self.__volume

  @property
  def price(self):
    return self.__price
  @price.setter
  def price(self, sum):
    self.__price = sum

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
    return f"Printer '{self.__name}', sold at min. ${self.price * 1.31}, ID#{self.ID}, uses {self.volume} of space"

  @property
  def max_paper_size(self):
    return self.__max_paper_size

class OECopier(OEScanner, OEPrinter)

def oewh_test():
  oep = OEPrinter("gnusmas", "s00", 1000, 30*40*45)
  print (oep)
  try:
    oep.ID = ".02"
  except Exception as e:
    print (e)

oewh_test()
