
def task_1():
  ls0 = list([12, "string", True, {"key0": (lambda x,y: x * y)}, {7, 1, 8}, lambda x,y: x ** y])
  for entry in ls0:
    print(type(entry))

def task_2():
  ls0 = list()
  for i in range(5):
    res = int(input("Hey dude, u wanna gimme 'int' now: "))
    ls0.append(res)
  print (f"Got {ls0} from user")
  for ind, val in enumerate(ls0):
    if ind % 2 != 0:
      ls0[ind-1], ls0[ind] = ls0[ind], ls0[ind-1]
  print(f"After all it's {ls0}")

def task_3():
  seasons = {'winter': [11, 0, 1], 'spring': [2, 3, 4], 'summer': [5, 6, 7], 'fall': [8, 9, 10],}
  mon = int(input('Gimme month as int 0-11: '))
  res = ""
  for ssn in seasons:
    # print (ssn)
    if mon in seasons[ssn]:
      res = ssn
      break
  print(f"User said {res}")

def task_4():
  frase = input("Hey write me several words with spaces: ")
  words = frase.split(" ")
  for index, word in enumerate(words):
    print(f"{index} is '{word[0:10]}'")

def task_5():
  print("Now you put in some nums and if wanna quit press any alphaKey")
  lst = list()
  while True:
    num = input("Your number: ")
    if num.isalpha():
      break
    elif num.isnumeric():
      intnum = int(num)
      if len(lst) == 0 or (len(lst) > 0 and intnum > max(lst)):
        lst.append(intnum)
      else:
        if num in lst:
          last_pos = lst.index(intnum)
          lst.insert(last_pos, intnum)
        else:
          ind = 0
          for ind, val in enumerate(lst):
            if val > intnum:
              break
          lst.insert(ind, intnum)
  print(f"User quitted at \n\t{lst[::-1]}")

def task_6():
  print("Lets list the goods: ")
  offset = 0
  goods = list()
  while True:
    inp = input("Put in new goods' name or (~ Enter) to quit: ")
    if inp == "~":
      break
    else:
      price = input("Price: ")
      while(price.isnumeric() != True):
        price = input("Price should be a number: ")
      qty = input("Qty: ")
      while(price.isnumeric() != True):
        price = input("Quantity should be a number: ")
      units = input (f"What do we call units for {inp}: ")
      gs = (offset, {'name': inp, 'price': int(price), 'qty': int(qty), 'units': units})
      goods.append(gs)
      offset += 1

  ks = goods[0][1].keys()
  ana = {}
  for k in ks:
    ana[k] = []

  for unit in goods:
    for k in ks:
      ana[k].append(unit[1][k])

  print("Goods are:")
  for unit in goods:
    print(f"\t{unit[0]} ==> {unit[1]}")
  
  print("\n\nAnalytics:")
  for k in ana:
    print (f"\t\"{k}\" ==> {ana[k]}")

task_1()
task_2()
task_3()
task_4()
task_5()
task_6()
