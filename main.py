# Importing the all the necessary libraries
from tkinter import *


def add_item(entry: Entry, listbox: Listbox):
    new_tasks = entry.get()

    # Check if user input a valid task not just spaces
    if new_tasks.isspace():
        pass
    else:
        listbox.insert(END, new_tasks)

        with open('D:/Projects_HHY/pythonProject - To Do List/tasks.txt', 'a') as tasks_list_file:
            tasks_list_file.write(f'{new_tasks}\n')


def delete_item(listbox: Listbox):
    with open('D:/Projects_HHY/pythonProject - To Do List/tasks.txt', 'r') as tasks_list_file:
        lines = tasks_list_file.readlines()
    with open('D:/Projects_HHY/pythonProject - To Do List/tasks.txt', 'w') as tasks_list_file:
        for line in lines:
            if listbox.get(ACTIVE) == line:  # Compare the selected task to delete up until the character
                lines.remove(line)
            else:

                # Updates the text file itself after removing the selected task to fix the bug where when remove task
                # button is pressed, instead of removing it will write in the whole same task list into the file again
                # resulting in doubled the same task lists (you can try to remove the else statement here and put the
                # .write method outside the if loop to experience this bug)
                tasks_list_file.write(line)

    listbox.delete(ACTIVE)  # Visually remove the current selected task to remove


# Initializing the to do list GUI window
root = Tk()
root.title("Brandon's Todo List")
root.geometry('600x800')
root.resizable(0, 0)
root.config(bg='Black')

# Heading label
Label(root, text='Brandon To Do List', font=('Comic Sans MS', 25),
      wraplength=1000, fg='White', bg='Black', anchor=CENTER).place(x=160, y=20)

# Listbox with all the tasks that's scrollable
tasks = Listbox(root, bg='Black', fg='White', font=('Helvetica', 15), height=24, width=50)

scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=560, y=100, height=580)

tasks.config(yscrollcommand=scroller.set)

tasks.place(x=25, y=100)

# Adding items to the ListBox
with open('D:/Projects_HHY/pythonProject - To Do List/tasks.txt', 'r') as tasks_list:
    lines = tasks_list.readlines()
for task in lines:
    tasks.insert(END, task)

# Creating the Entry widget so that user can enter new tasks with using widget text box
new_item_entry = Entry(root, width=90)
new_item_entry.place(x=25, y=710)

# Creating the add and delete task button
add_btn = Button(root, text='Add a task', bg='Azure', width=20, font=('Helvetica', 15),
                 command=lambda: add_item(new_item_entry, tasks))
add_btn.place(x=25, y=750)
dlt_btn = Button(root, text='Remove a task', bg='Azure', width=20, font=('Helvetica', 15),
                 command=lambda: delete_item(tasks))
dlt_btn.place(x=340, y=750)

# Finalizing the window
root.update()
root.mainloop()
