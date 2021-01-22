from time import sleep, monotonic

class TrafficLight:
  __color = -1

  def running(self):
    color_tijd = self.__change_color()
    print(f"Currently color is {color_tijd[0]}")
    t0 = monotonic()
    sleep (color_tijd[1])
    t1 = monotonic()
    print(f"\tPassed {color_tijd[1]} or {t1 - t0} seconds")

  def __change_color(self):
    self.__color += 1
    if self.__color > 2: self.__color = 0
    colors = ["red", "yellow", "green"]
    times = [7, 2, 10]
    return colors[self.__color], times[self.__color]

class Road:
  _length = 0
  _width = 0
  def __init__(self, length, width):
    self._length = length
    self._width = width
  
  def need_asfalt(self, asfalt_weight=25, thickness=5):
    return self._width * self._length * asfalt_weight * thickness

class Worker:
  name = ""
  surname = ""
  position = ""
  _income = {'wage': -1, 'bonus': -1}

class Position (Worker):

  def __init__(self):
    self.get_full_name()
    self.get_total_income()

  def get_full_name(self):
    self.name = input("Worker's name: ")
    self.surname = input("Worker's surname: ")

  def get_total_income(self):
    s0 = input("Provide wage as integer: ")
    try:
      self._income['wage'] = int(s0)
    except ValueError:
      print("The wage is to be numeric integer value! Please, retry")
    
    s1 = input("Provide bonus as integer: ")
    try:
      self._income['bonus'] = int(s1)
    except ValueError:
      print("The bonus is to be numeric integer value! Please, retry")

  def print_data(self):
    if self._income['wage'] != -1:
      print(f"Currently {self.name} {self.surname} earns {self._income['wage'] + self._income['bonus']}")
    else:
      self.get_total_income()

class Car:
  speed = 0
  color = ""
  name = ""
  goes = False
  is_police = False

  def __init__(self, color='red', name='mazda', is_police=False):
    self.color = color.capitalize()
    self.name = name.capitalize()
    self.is_police = is_police

  def show_speed(self):
    print(f"{self.color} {self.name} moves at {self.speed} km/h now")

  def go(self, speed=100):
    try:
      self.speed = int(speed)
      self.goes = True
    except ValueError:
      print (f"{self.color} {self.name} failed to start")
      return False
    print(f"{self.color} {self.name} started")
    return True

  def set_speed(self, speed):
    try:
      self.speed = int(speed)
      print(f"Setting speed to {self.speed} km/h")
    except ValueError:
      pass

  def stop(self):
    if self.goes:
      print(f"{self.color} {self.name} stopped")
    else:
      print("Cannot stop without going")
      return False
    return True

  def turn(self, direction):
    if (direction in ['right', 'left']):
      print(f"{self.color} {self.name} turns {direction}")
    else:
      print(f"No rotation in direction {direction}")
      return False
    return True

class TownCar(Car):
  def __init__ (self, color='white', name='mazda'):
    super().__init__(color, name, False)

  def show_speed(self):
    if self.speed > 60:
      print(f"du overstiger fartsgrensen".upper())
    super().show_speed()

class SportCar(Car):
  def __init__ (self, color='silver', name='mazeratti'):
    super().__init__(color, name, False)

class WorkCar(Car):
  def __init__ (self, color='orange', name='traktor'):
    super().__init__(color, name, False)

  def show_speed(self):
    if self.speed > 40:
      print(f"du overstiger fartsgrensen".upper())
    super().show_speed()

class PoliceCar(Car):
  def __init__ (self, color='white-blue', name='mersedez'):
    super().__init__(color, "police " + name, True)

  def show_speed(self):
    if self.speed > 100:
      print(f"you can do even more!".upper())
    super().show_speed()

def cars_test():
  tc = TownCar(); sc = SportCar(); wc = WorkCar(); pc = PoliceCar();
  tc.go(); 
  # sc.go(); 
  wc.go(); 
  pc.go()
  tc.show_speed(); 
  sc.show_speed(); 
  wc.show_speed(); 
  pc.show_speed(); 
  tc.set_speed(59); 
  wc.set_speed(39); 
  pc.set_speed(1000); 
  tc.show_speed(); 
  sc.show_speed(); 
  wc.show_speed(); 
  pc.show_speed(); 
  pc.turn('right')
  sc.turn("down")
  pc.stop()
  sc.stop() #won't stop, not running

class Stationery:
  title = ""

  def __init__(self, name=""):
    self.title = name

  def draw (self):
    if self.title == "": 
      print("Stationery not initialised")
      return

    print("Запуск отрисовки")
    print (f"{self.title.capitalize()} draws")

class Pen(Stationery):
  def __init__(self):
    super().__init__("pen")

class Pencil(Stationery):
  def __init__(self):
    super().__init__("pencil")

class Handle(Stationery):
  def __init__(self):
    super().__init__("handle")

def stat_test():
  pen = Pen()
  pencil = Pencil()
  handle = Handle()
  stat = Stationery()
  pen.draw()
  pencil.draw()
  handle.draw()
  stat.draw()

tl = TrafficLight()
for i in range(5): tl.running()

rd = Road(5000, 20)
print(f"Asfalt needed: {rd.need_asfalt() / 1000} tons")

wp = Position()
wp.print_data()

cars_test()

stat_test()
