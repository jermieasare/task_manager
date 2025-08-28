import tkinter as tk
from tkinter import messagebox
from functools import partial
import commands

# Handle update task and update the UI  
def handle_update(id, title, app):
    if not title:
        messagebox.showerror(
            title="Update Task",
            message="Task title cannot be empty",
            parent=app)
    else:
        commands.update_task(id, {"title": title})
        show_all_tasks_frame(app)

# handle delete task and update the UI
def handle_delete(id, app):
    commands.delete_task(id)
    show_all_tasks_frame(app)

# Function to handle task submission
def submit_task(title, app):
    if not title:
        messagebox.showerror(
            title="Add Task",
            message="Cannot add empty task",
            parent=app)
    else:
        commands.save_task({"title": title})
        show_all_tasks_frame(app)

# Function to display the edit task frame
def show_edit_task_frame(task, app):
    frame= tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    label=tk.Label(master=frame, text=f"Edit Task: {task['title']}")
    label.grid()

#Add an entry widget and show the task title
    entry=tk.Entry(master=frame)
    entry.insert(0,task["title"])
    entry.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(5,10))

#Add a button with text update for saving changes
    update_btn=tk.Button(
        master=frame,
        text="Update",command=lambda: handle_update (task["_id"],entry.get(), app))
    update_btn.grid(row=2, column=1)
    
#Add a button with text Back/Cancel for removing the frame
    cancel_btn=tk.Button(
        master=frame,
        text="Back", 
        command=lambda: frame.destroy())
    cancel_btn.grid(row=2, column=0)

    frame.tkraise()

# Function to display the add task frame
def show_add_task_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Add label and entry field
    label = tk.Label(master=frame, text="What do you want to do?")
    label.grid()
    entry = tk.Entry(master=frame)
    entry.grid()

# Add submit button
    btn=tk.Button(
        master=frame, 
        text="Submit", 
        command=lambda: submit_task(entry.get(), app))
    btn.grid()

    frame.tkraise()

# Function to display all tasks
def show_all_tasks_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Get all tasks from database
    tasks = commands.get_tasks().to_list()
    for task in tasks:
        checkbtn = tk.Checkbutton(
            master=frame, 
            text=task ["title"])
        checkbtn.grid(row=tasks.index(task), column=0)
# Create an edit button for each task
        edit_btn = tk.Button(
            master=frame,
            text="Edit", command=partial(show_edit_task_frame, task,app))
        edit_btn.grid(row=tasks.index(task), column=1)

#create a delete button for each task
        delete_btn=tk.Button(
            master = frame, 
            text= "Delete", 
            command=partial(handle_delete, 
            task["_id"], app))
        delete_btn.grid(row=tasks.index(task), column=2)

# Add button to add new task
    add_btn =tk.Button(
        master=frame, 
        text="Add Task", 
        command= lambda: show_add_task_frame(app))
    add_btn.grid(row=len(tasks)+1, column=0)

#show the frame with the above tasks and make it visible
    frame.tkraise()


