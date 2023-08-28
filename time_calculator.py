def add_time(start, duration, day = None):

  #spliting the inputs.

  start_time,meridiem = start.split()
  start_hour,start_minutes = start_time.split(":")
  duration_hour,duration_minutes = duration.split(":")

  #variables nedded for later lines :

  new_hour = 0
  n = 0
  weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ,"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  #the actual counting algorithm :

  #the minutes algo.

  new_minutes = int(start_minutes) + int(duration_minutes)

  if new_minutes >= 60 :
    new_minutes = new_minutes - 60
    new_hour = 1

  if new_minutes < 10 :
    new_minutes = "0" + str(new_minutes)

  #the hours and merediem algo.

  new_hour = new_hour + int(start_hour) + int(duration_hour)

  substraction = True

  while substraction :
    if new_hour > 12 :
      new_hour = new_hour - 12
      if meridiem == "PM":
        meridiem = "AM"
        #the "n days later" algo (counting).
        n = n + 1
      elif meridiem == "AM":
        meridiem = "PM"

    elif new_hour < 12 :
      substraction = False

    elif new_hour == 12 :
      new_hour = 12
      if meridiem == "PM":
        meridiem = "AM"
        #the "n days later" algo (counting).
        n = n + 1
      elif meridiem == "AM":
        meridiem = "PM" 
      substraction = False

  #the weekday algo.
  if day is not None :
    day = day.lower()
    day = day.replace(day[0],day[0].upper())
    weekday_index = weekdays.index(day)
    weekday = weekdays[weekday_index + n]

  # "n days later" algo mixed with return statements
  if day is None :
    if n == 0 :
      return(f"{new_hour}:{new_minutes} {meridiem}")
    elif n == 1 :
      return(f"{new_hour}:{new_minutes} {meridiem} (next day)")
    elif n > 1 :
      n_days = f"({n} days later)"
      return(f"{new_hour}:{new_minutes} {meridiem} {n_days}")
  else :
    if n == 0 :
      return(f"{new_hour}:{new_minutes} {meridiem}, {weekday}")
    elif n == 1 :
      return(f"{new_hour}:{new_minutes} {meridiem}, {weekday} (next day)")
    elif n > 1 :
      n_days = f"({n} days later)"
      return(f"{new_hour}:{new_minutes} {meridiem}, {weekday} {n_days}")

  

  
