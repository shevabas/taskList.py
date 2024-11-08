import time

fileLocation = //"location of your text file"

with open(fileLocation, "r") as file:
  contents = file.readlines()
# Pause function
def pause():
  input("Press enter to move on\n")

##############################################################################################################
# 1. adding new task to list
def addNewTask(taskName, dueDate, timeDue, notes):
  if notes == "":
    notes = "NO NOTES"
  newTask = f'{taskName}\n{dueDate}\n{timeDue}\n{notes}\n'
  with open(fileLocation, "a") as file:
    file.write(newTask)
  time.sleep(0.4)
  print(f'\nThe task you added:\n{newTask}')
  time.sleep(4)

##############################################################################################################
# 2. removing task from list
def removeTask(taskName):
  try:
    # updating contents before removing task
    with open(fileLocation, "r") as file:
      contents = file.readlines()

    taskFound = False
    for line in contents:
      if taskName.strip().lower() in line.strip().lower():
        taskIndex = contents.index(line)
        taskFound = True
        break
    if taskFound == False: 
      print(f'{taskName} not found.')
      time.sleep(2)
      return

    # replace these lines with None, so later when writing back it will skip these lines
    contents[taskIndex] = None
    contents[taskIndex+1] = None
    contents[taskIndex+2] = None
    contents[taskIndex+3] = None
    # writing back only lines where the values DOES NOT equal None
    with open(fileLocation, "w") as file:
      file.writelines(line for line in contents if line is not None and line.strip())

    time.sleep(0.3)
    print(f'{taskName} and related contents were removed from your task list.')
    time.sleep(4)
  except:
    print("Problem occured (most likely the task was not found, although not always)")
    time.sleep(2)

##############################################################################################################
# 3. edit task
def editTask(taskName):
  try: 
    # updating contents before editing task
    with open(fileLocation, "r") as file:
      contents = file.readlines()

    # finding what index taskName is at and index of date/time due and notes
    taskFound = False
    for line in contents:
      if taskName.strip().lower() in line.strip().lower():
        taskIndex = contents.index(line)
        taskFound = True
        break
    if taskFound == False: 
      print(f'{taskName} not found.')
      time.sleep(2)
      return
    dueDate = contents[taskIndex+1]
    timeDue = contents[taskIndex+2]
    notes = contents[taskIndex+3]

    # asking if wanting to change value, reminding them of old value, and then updating the value as the new one 
    # if they dont wanna update, it stays the same (thats why we had to find/declare variable values before this)
    if input("Do you want to edit the name (y/n)?: ") == "y":
      fullTaskName = contents[taskIndex]
      print(f'  (Task name: {fullTaskName.strip()})')
      taskName = input("  What is the new name of your task?: ")
      contents[taskIndex] = taskName + "\n"
    if input("Do you want to edit the due date (y/n)?: ") == "y":
      print(f'  (Due Date: {dueDate.strip()})')
      dueDate = input("  What is the new due date?: ")
      contents[taskIndex+1] = dueDate + "\n"
    if input("Do you want to edit the time due (y/n)?: ") == "y":
      print(f'  (Time due: {timeDue.strip()})')
      timeDue = input("  What is the new time it's due?: ")
      contents[taskIndex+2] = timeDue + "\n"
    if input("Do you want to edit your notes (y/n)?: ") == "y":
      print(f'  (Your notes: {notes.strip()})')
      notes = input("  What are the new task notes?: ")
      contents[taskIndex+3] = notes + "\n"

    # updating contents and printing it out after a delay so it looks more natural
    with open(fileLocation, "w") as file:
      file.writelines(contents)
    time.sleep(0.4)
    print("\nHere is your new task: ")
    time.sleep(0.6)
    print(f'Task name: {taskName.strip()}\nDate due: {dueDate.strip()}\nTime Due: {timeDue.strip()}\nNotes: {notes.strip()}')
    pause()
    # time.sleep(5)
  except:
    print("Error occured (most likely task was not found)")
    time.sleep(2)
  
##############################################################################################################
# 4. reading all tasks and dates
def displayAllTasks():
  # updating value of contents
  with open(fileLocation, "r") as file:
    contents = file.readlines()
  
  print("Reading all tasks")
  time.sleep(0.5)
  totalLines = len(contents) -1

  task = 1
  number = 1
  while task < totalLines:
    print(f'TASK {number}:\n{contents[task]}{contents[task+1]}{contents[task+2]}{contents[task+3]}')
    task += 4
    number+=1
    pause()
  print("All tasks shown")
  time.sleep(1.5)

##############################################################################################################
# 5. reading only tasks names
def readTaskNames():
  # updating value of contents
  with open(fileLocation, "r") as file:
    contents = file.readlines()

  task = 1
  number = 1
  totalLines = len(contents) -1

  while task < totalLines:
    print(f'Task {number}: {contents[task].strip()}')
    task += 4
    number += 1
  pause()
  # time.sleep(5)

##############################################################################################################
# 6. read a specific task
def readATask(taskName):
  # updating value of contents
  with open(fileLocation, "r") as file:
    contents = file.readlines()

  for line in contents:
    if taskName.strip().lower() in line.strip().lower():
      locationToReadAt = contents.index(line)
  print(f'Task Name:  {contents[locationToReadAt].strip()}')
  print(f'Due Date:   {contents[locationToReadAt+1].strip()}')
  print(f'Time Due:   {contents[locationToReadAt+2].strip()}')
  print(f'Notes:      {contents[locationToReadAt+3].strip()}')
  pause()
  # time.sleep(5)



##############################################################################################################


while True:
  print("\nMain menu")
  print("1. Add new task")
  print("2. Remove a task")
  print("3. Edit task")
  print("4. Read all tasks")
  print("5. Read all tasks names")
  print("6. Read specific task")
  print("7. Leave")
  option = int(input("\nWhat would you like to do?: "))
  
  if option == 1:
    with open(fileLocation, "r") as file:
      contents = file.readlines()
    while True:
      taskName = input("What is the name of the task?: ")
      
      # checking duplicate
      duplicateTask = False
      for line in contents:
        if taskName.strip().lower() == line.strip().lower():
          print("That task already exists")
          duplicateTask = True
          break
      
      if duplicateTask == False:
        dueDate = input("What day is it due?: ")
        timeDue = input("What time is it due?: ")
        notes = input("Any notes to add? (press enter if not): ")
        addNewTask(taskName, dueDate, timeDue, notes)
        break
  
  elif option == 2:
    taskName = input("What task do you want to remove?: ")
    removeTask(taskName)
  
  elif option == 3:
    taskName = input("What is the name of the task you want to edit?: ")
    editTask(taskName)

  elif option == 4:
    displayAllTasks()
  
  elif option == 5:
    readTaskNames()
  
  elif option == 6:
    taskName = input("What is the name of the task?: ")
    readATask(taskName)
  
  else:
    print("Leaving task list")
    break