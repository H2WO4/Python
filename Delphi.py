#!/bin/python3
import json
import tkinter as tk
import tkinter.filedialog as filedialog
from typing import Any

# Define classes
class Student:
	def __init__(self, family_name: str, first_name: str, grade: int = 0) -> None:
		self.family_name = family_name
		self.first_name  = first_name
		self.grade       = grade

""" Graphical """
# Setup
main = tk.Tk()
main.title("Database")
main.geometry("512x384")

last_selection: str = ""

# List
def select_student(*_):
	global last_selection

	selection: tuple[int, ...] = data_list.curselection() # type: ignore
	if selection == ():
		return

	full_var = data_list.get(0, tk.END) # type: ignore
	last_selection = full_var[selection[0]] # type: ignore

	student = get_curr_student()

	family_name_entry.delete(0, tk.END)
	family_name_entry.insert(0, student.family_name)

	first_name_entry.delete(0, tk.END)
	first_name_entry.insert(0, student.first_name)

	grade_entry.delete(0, tk.END)
	grade_entry.insert(0, str(student.grade))

def update_entries():
	data_list.delete(0, tk.END)
	for i, student in enumerate(sorted(student_list.keys())):
		data_list.insert(i, student)

data_list = tk.Listbox(master=main, width=16, height=12)
data_list.place(x=64, y=64)
data_list.bind("<<ListboxSelect>>", select_student) # type: ignore

# Family name
def change_family_name(*_) -> None:
	global last_selection

	student = get_curr_student()

	del student_list[student.family_name]
	family_name = family_name_entry.get().upper()
	student.family_name = family_name
	student_list[family_name] = student

	family_name_entry.delete(0, tk.END)
	family_name_entry.insert(0, family_name)

	last_selection = family_name
	update_entries()

family_name_entry = tk.Entry(master=main, width=16)
family_name_entry.place(x=260, y=64)
family_name_entry.bind("<FocusOut>", change_family_name) # type: ignore

# First name
def change_first_name(*_) -> None:
	student = get_curr_student()
	student.first_name = first_name_entry.get()

	update_entries()

first_name_entry = tk.Entry(master=main, width=16)
first_name_entry.place(x=260, y=96)
first_name_entry.bind("<FocusOut>", change_first_name) # type: ignore

# Grade
def change_grade(*_) -> None:
	student = get_curr_student()
	try:
		grade = int(grade_entry.get())
		student.grade = grade
	except ValueError:
		return

	update_entries()

grade_entry = tk.Entry(master=main, width=16)
grade_entry.place(x=260, y=128)
grade_entry.bind("<FocusOut>", change_grade) # type: ignore


# Add
def new_student(*_):
	family_name = "LOREM"
	first_name =  "Ipsum"

	full_var = data_list.get(0, tk.END) # type: ignore
	if family_name in full_var:
		suffix = 1
		while f"{family_name}{suffix}" in full_var:
			suffix += 1
		
		family_name = f"{family_name}{suffix}"

	data_list.insert(tk.END, family_name)
	student_list[family_name] = Student(family_name, first_name)

load_file_button = tk.Button(master=main, width=8, height=1, text="Add", command=new_student) # type: ignore
load_file_button.place(x=260, y=240)

# Remove
def del_student(*_):
	student = get_curr_student()
	del student_list[student.family_name]

	family_name_entry.delete(0, tk.END)
	first_name_entry.delete(0, tk.END)

	update_entries()

del_button = tk.Button(master=main, width=8, height=1, text="Remove", command=del_student) # type: ignore
del_button.place(x=360, y=240)
data_list.bind("<Delete>", del_student) # type: ignore


# Load
def load_file():
	global student_list

	filename = filedialog.askopenfilename()
	if filename.endswith(".save"):
		student_list = { }

		with open(filename, 'rb') as f:
			quantity = int.from_bytes(f.read(2), byteorder='big')

			for _ in range(quantity):
				len_family_name = int.from_bytes(f.read(2), byteorder='big')
				
				family_name = f.read(len_family_name).decode('utf_8')

				len_first_name = int.from_bytes(f.read(2), byteorder='big')
				first_name = f.read(len_first_name).decode('utf_8')

				add_student(family_name, first_name)	
	
	elif filename.endswith(".json"):
		student_list = { }

		with open(filename, 'r') as f:
			data: dict[str, Any] = json.load(f)

			for student in data.values():
				add_student(student["family_name"], student["first_name"], student["grade"])

load_file_button = tk.Button(master=main, width=8, height=1, text="Load", command=load_file) # type: ignore
load_file_button.place(x=260, y=276)

# Save
def save_file():
	filename = filedialog.asksaveasfilename(filetypes=[("Binary", ".save"), ("JSON", ".json")])

	if filename.endswith(".save"):
		with open(filename, 'wb') as f:
			f.write(len(student_list).to_bytes(2, byteorder='big'))

			for student in student_list.values():
				f.write(len(student.family_name).to_bytes(2, byteorder='big'))
				f.write(student.family_name.encode('utf-8'))

				f.write(len(student.first_name).to_bytes(2, byteorder='big'))
				f.write(student.first_name.encode('utf-8'))

				f.write(student.grade.to_bytes(2, byteorder='big'))
	
	elif filename.endswith(".json"):
		with open(filename, 'w') as f:
			json.dump({key: val.__dict__ for key, val in student_list.items()}, f, indent=2)

save_file_button = tk.Button(master=main, width=8, height=1, text="Save", command=save_file) # type: ignore
save_file_button.place(x=360, y=276)

""" Functional """
# Students
student_list: dict[str, Student] = { }
def add_student(family_name: str, first_name: str, grade: int = 0) -> None:
	data_list.insert(tk.END, family_name) # type: ignore
	student_list[family_name] = Student(family_name, first_name, grade)

def get_curr_student() -> Student:
	global last_selection
	return student_list[last_selection]

main.mainloop()
