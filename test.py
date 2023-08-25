# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoFile.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Nicole Tenev, 8/18/23, added new functionalities):
# RRoot, 1.1.2030, Created started script
# Nicole Tenev, 8/18/23, Modified code to complete assignment 06
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection


# Processing  --------------------------------------------------------------- #
class Processor:
    """Performs Processing tasks"""

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """Reads data from a file into a list of dictionary rows"""
        list_of_rows.clear()  # clear current data
        with open(file_name, "r") as file:
            for line in file:
                task, priority = line.strip().split(",")
                row = {"Task": task, "Priority": priority}
                list_of_rows.append(row)
        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """Adds data to a list of dictionary rows"""
        row = {"Task": task, "Priority": priority}
        list_of_rows.append(row)
        return list_of_rows

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """Removes data from a list of dictionary rows"""
        list_of_rows = [row for row in list_of_rows if row["Task"].lower() != task.lower()]
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """Writes data from a list of dictionary rows to a File"""
        with open(file_name, "w") as file:
            for row in list_of_rows:
                file.write(f"{row['Task']},{row['Priority']}\n")
        return list_of_rows


# Presentation (Input/Output)  -------------------------------------------- #

class IO:
    """Performs Input and Output tasks"""

    @staticmethod
    def output_menu_tasks():
        """Display a menu of choices to the user"""
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File
        4) Exit Program
        ''')

    @staticmethod
    def input_menu_choice():
        """Gets the menu choice from a user"""
        choice = input("Which option would you like to perform? [1 to 4] - ").strip()
        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """Shows the current Tasks in the list of dictionaries rows"""
        print("******* The current tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")

    @staticmethod
    def input_new_task_and_priority():
        """Gets task and priority values to be added to the list"""
        task = input("Enter a new task: ").strip()
        priority = input("Enter the priority for the task: ").strip()
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """Gets the task name to be removed from the list"""
        task = input("Enter the task name to remove: ").strip()
        return task


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name=file_name_str, list_of_rows=table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 Show current data
    IO.output_current_tasks_in_list(list_of_rows=table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str == '1':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()
        table_lst = Processor.add_data_to_list(task=task, priority=priority, list_of_rows=table_lst)

    elif choice_str == '2':  # Remove an existing Task
        task = IO.input_task_to_remove()
        table_lst = Processor.remove_data_from_list(task=task, list_of_rows=table_lst)

    elif choice_str == '3':  # Save Data to File
        table_lst = Processor.write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)
        print("Data Saved!")

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop
