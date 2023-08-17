# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (NTenev,8-14-2023,What):
# RRoot,1.1.2030,Created started script
# <NTenev>,<D8-14-2023>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries of rows
# TODO: Add Code Here
try:
    file = open(objFile, "r")
    for line in file:
        task, priority = line.strip().split(",")
        dicRow = {"Task": task, "Priority": priority}
        lstTable.append(dicRow)
    file.close()
except FileNotFoundError:
    print("No existing data found. Starting with an empty list.")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        for row in lstTable:
            print(f"Task: {row['Task']}, Priority: {row['Priority']}")

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        task = input("Enter task: ")
        priority = input("Enter priority: ")
        dicRow = {"Task": task, "Priority": priority}
        lstTable.append(dicRow)

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        task_to_remove = input("Enter task to remove: ")
        for row in lstTable:
            if row['Task'] == task_to_remove:
                lstTable.remove(row)
                print(f"Task '{task_to_remove}' removed.")
                break
        else:
            print(f"Task '{task_to_remove}' not found.")

    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        file = open(objFile, "w")
        for row in lstTable:
            file.write(f"{row['Task']},{row['Priority']}\n")
        file.close()
        print("Data saved to file.")

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Exiting program...")
        break