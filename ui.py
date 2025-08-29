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
    frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    label=tk.Label(master=frame, text="Edit Task", font=("Arial", 14, "bold"))
    label.grid(row=0, column=0, columnspan=2, pady=(10))

#Add an entry widget and show the task title
    entry=tk.Entry(master=frame, width=40)
    entry.insert(0,task["title"])
    entry.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(5))

#Add a button with text update for saving changes
    update_btn=tk.Button(
        master=frame,width=8,
        text="Update",command=lambda: handle_update (task["_id"],entry.get(), app))
    update_btn.grid(row=2, column=1, pady=10, sticky="e")
    
#Add a button with text Back/Cancel for removing the frame
    cancel_btn=tk.Button(
        master=frame,
        text="Back", 
        width=8,
        command=lambda: show_all_tasks_frame(app))
    cancel_btn.grid(row=2, column=0, pady=10, sticky="w")

    frame.tkraise()

# Function to display the add task frame
def show_add_task_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# Add label and entry field
    label = tk.Label(master=frame, text="Add New Task", font=("Arial", 14, "bold"))
    label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    entry = tk.Entry(master=frame, width=40)
    entry.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(5))

# Add submit button
    btn=tk.Button(
        master=frame,width=8, 
        text="Submit", 
        command=lambda: submit_task(entry.get(), app))
    btn.grid(row=2, column=0, pady=10, columnspan=2, sticky="e")

    frame.tkraise()

# Function to display all tasks
def show_all_tasks_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    label=tk.Label(master=frame, text="All Tasks", font=("Arial", 14, "bold"))
    label.grid(row=0, column=0, columnspan=3, pady=(0,10))
    

# Get all tasks from database
    tasks = commands.get_tasks().to_list()
    for task in tasks:
        checkbtn = tk.Checkbutton(
            master=frame, 
            text=task ["title"])
        checkbtn.grid(row=tasks.index(task)+1, column=0)
# Create an edit button for each task
        edit_btn = tk.Button(
            master=frame, width=8,
            text="Edit", command=partial(show_edit_task_frame, task,app))
        edit_btn.grid(row=tasks.index(task)+1, column=1, padx=5, pady=5)

#create a delete button for each task
        delete_btn=tk.Button(
            master = frame, width=8,
            text= "Delete", 
            command=partial(handle_delete, 
            task["_id"], app))
        delete_btn.grid(row=tasks.index(task)+1, column=2, padx=5, pady=5)

# Add button to add new task
    add_btn =tk.Button(
        master=frame, width=12,
        text="Add Task", 
        command= lambda: show_add_task_frame(app))
    add_btn.grid(row=len(tasks)+1, column=0, pady=15, columnspan=3,)

#show the frame with the above tasks and make it visible
    frame.tkraise()


