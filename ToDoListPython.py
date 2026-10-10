#Makes a list to store tasks
taskList = []

#Adds tasks to list
def addTask(task):
   taskList.append(task)
   print(f"Added task: {task}\n")

#Removes task from list
def removeTask(task):
   #Checks if list is empty (no tasks)
   if len(taskList) == 0:
      print("No tasks to remove. Add a task to get started!\n")
   #If task is not in list (so it wont break)
   elif task not in taskList:
      print("Task not in list\n")
   #Removes task
   else:
      taskList.remove(task)
      print(f"Removed task: {task}\n")

#View full list
def viewList():
   #Checks if list is empty
   if len(taskList) == 0:
      print("List is empty. Add a task to get started!\n")
   #Loops through and prints list
   else:
      print("========Printing List========")
   
   for task in taskList:
      print(f"- {task}")

#Save
def saveList():
   #Open/Create file in write mode
   with open("ToDoList.txt", "w", encoding="utf-8") as file:
      #Writes list to file
      for task in taskList:
         file.write(task + "\n")
   print("List saved!\n")

#Load
def loadList():
   try:
      #Open file in read mode
      with open("ToDoList.txt", "r", encoding="utf-8") as file:
         #Adds lines to list
         for line in file:
            task = line.strip()#.strip() removes newline char and whitespace
            taskList.append(task)
   
   #When loading without a save file
   except FileNotFoundError:
      print("No save file. Creating new list!")

#Always loads list before starting
loadList()

#First thing user sees when opening
print("Welcome to Your To-Do List! Choose an Option to Get Started\n")

#Gameplay loop
while True:
   #Options
   print("\n1. Add a task")
   print("2. Remove a task")
   print("3. View list")
   print("4. Save and Quit\n")  

   option = int(input("Choose a number:\n"))

   #Add task
   if option == 1:
      task = input("Enter task to add:\n")
      addTask(task)
   
   #Remove task
   elif option == 2:
      task = input("Enter task to remove:\n")
      removeTask(task)  
      
   #View list
   elif option == 3:
      viewList()
   
   #Save and quit
   elif option == 4:
      saveList()
      print("Goodbye!")
      break
   
   else:
      print("Not an available option\n")
