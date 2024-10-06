import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk()
root.title("Task list")
root.configure(background="LightSlateBlue")

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        update_task_count()

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)
        update_task_count()

def mark_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.itemconfig(selected_task, bg='lawn green')

def edit_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        new_task = task_entry.get()
        if new_task:
            task_listbox.delete(selected_task)
            task_listbox.insert(selected_task, new_task)
            task_entry.delete(0, tk.END)

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Info", "Tasks saved successfully!")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        for task in tasks:
            task_listbox.insert(tk.END, task.strip())
        update_task_count()

def update_task_count():
    total_tasks = task_listbox.size()
    done_tasks = sum(1 for i in range(total_tasks) if task_listbox.itemcget(i, 'bg') == 'lawn green')
    task_count_label.config(text=f"Total tasks: {total_tasks}, Done tasks: {done_tasks}")

text1 = tk.Label(root, text='Введите вашу задачу', bg='light blue')
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg='DeepSkyBlue3')
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text='Add task', command=add_task)
add_task_button.pack(pady=5)

delete_button = tk.Button(root, text='Delete task', command=delete_task)
delete_button.pack(pady=5)

done_button = tk.Button(root, text='Mark done task', command=mark_task)
done_button.pack(pady=5)

edit_button = tk.Button(root, text='Edit task', command=edit_task)
edit_button.pack(pady=5)

save_button = tk.Button(root, text='Save tasks', command=save_tasks)
save_button.pack(pady=5)

load_button = tk.Button(root, text='Load tasks', command=load_tasks)
load_button.pack(pady=5)

task_count_label = tk.Label(root, text='', bg='light blue')
task_count_label.pack(pady=5)

text2 = tk.Label(root, text='Список задач', bg='light blue')
text2.pack(pady=5)

task_listbox = tk.Listbox(root, height=10, width=50, bg='cornflower blue')
task_listbox.pack(pady=5)

load_tasks()  # загрузка задач при запуске программы

root.mainloop()


