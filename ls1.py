def q0():
  """ 1 """
  name = input ('Your name: ')
  age = int(input('Your age: '))
  name_age_dict = dict(name = name, age = age)

def q1():
  """ 2 """
  uts = int(input ('Input time in secs: '))
  hours = int(uts // 3600)
  hs_leftover = uts - (hours * 3600)
  minutes = int(hs_leftover // 60)
  seconds = int(hs_leftover - (minutes * 60))
  print (f"Current time: {hours:02}:{minutes:02}:{seconds:02}\n")

def q2():
  """ 3 """
  suin = input('Now give me a num: ')
  n0 = int(suin)
  n1 = int(f"{suin*2}")
  n2 = int(f"{suin*3}")
  snewnum = n0 + n1 + n2
  print(f"User gave {suin}, I return you {snewnum} as sum of {n0}, {n1} and {n2}")

def q3():
  """ 4 """
  posintstr = input ("Gimme a positive integer of any lenth (pls hyperf**k thee not)\n\t: ")
  tmp = 0
  for ch in posintstr:
    if int(ch) > tmp:
      tmp = int(ch)
  print (f"Biggest number in your num is {tmp}\n")

def q4():
  """ 5 """
  incs = int(input("Gimme incomes of the enterprize (as int): "))
  outs = int(input("Gimme expences of the enterprize (as int): "))
  revenue = incs - outs
  if revenue > 0:
    print(f"Gee your enterprizes profit counts to {str(revenue)}")
    print (f"\tRentability of your enterprize looks like {revenue/incs}")
    crew_count = int(input("\nHow many people do you hire (hopefully integer): "))
    print (f"\n\tIncome per crewman is {revenue / crew_count}")
  elif revenue < 0:
    print(f"Gee your enterprize kinna fails dude by {revenue}")
    print (f"\tRentability of your enterprize looks like {revenue/incs}, \nso you may just burn in hell and that's enough")
  elif revenue == 0:
    print(f"Gee you enterprize breaks even, not bad bro!")

def q5():
  """ 6 """
  first_day_results = int(input("~~~~~~~~~~~~\nNow how many kilometers did da dude ran aujourd'hui: "))
  necessary_distance = int(input("At which distance per day he may feel he works fine: "))
  if first_day_results > necessary_distance:
    print (f"Oh my - {first_day_results - necessary_distance} are you serious?")
  else:
    counter = 0
    next_day_result = first_day_results
    while next_day_result <= necessary_distance:
      next_day_result *= 1.1
      counter += 1
    print (f"The runner runs fine since day {counter}")

q0()
q1()
q2()
q3()
q4()
q5()
