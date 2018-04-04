import random
from tkinter import Tk, Label, Button, StringVar, DISABLED, NORMAL, END, W, E
from config import Config

class GUI:
	def __init__(self, master):
		self.master = master
		self.conf = Config()
		master.title(self.conf.TITLE)

		# Header Label
		self.header_label_text = StringVar()
		self.header_label_text.set(self.conf.PROG_NAME)
		self.header_label = Label(master, textvariable=self.header_label_text, font=('Arial', 45))

		# File Import Label
		self.file_label_text = StringVar()
		self.file_label_text.set("Select student list Excel file:")
		self.file_label = Label(master, textvariable=self.file_label_text, font=('Arial', 15, 'bold'))

		# File Import Button
		self.file_button = Button(master, text="Import List", command=self.select_list)

		# Students Label
		self.student_label = Label(master, text="Select a Student:", font=('Arial', 15, 'bold'))

		# Student List
		#self.student_list = []
		self.student_list = ['Something Weird', 'Someone Else', 'Who Else']

		self.header_label.grid(row=0, column=0, columnspan=5, sticky=W+E)
		self.file_label.grid(row=1, column=0, columnspan=2, sticky=W)
		self.file_button.grid(row=1, column=2, columnspan=1)
		self.student_label.grid(row=2, column=0, columnspan=1, sticky=W)
		#self.reset_button.grid(row=3, column=1)

	def render_student_combobox(self):
		self.selected_students = StringVar()
		self.students_combobox = ttk.Combobox(self.master, textvariable=self.selected_students)
		self.students_combobox['values'] = self.student_list
		self.students_combobox.bind("<<ComboboxSelected>>", self.newselection)

	def start(self):
		self.master.mainloop()

	def select_list(self):
		print('selecting list')

	def newselection(self, event):
		print(self.students_combobox.get())

	def guess_number(self):
		self.num_guesses += 1

		if self.guess is None:
			self.message = "Guess a number from 1 to 100"

		elif self.guess == self.secret_number:
			suffix = '' if self.num_guesses == 1 else 'es'
			self.message = "Congratulations! You guessed the number after %d guess%s." % (self.num_guesses, suffix)
			self.guess_button.configure(state=DISABLED)
			self.reset_button.configure(state=NORMAL)

		elif self.guess < self.secret_number:
			self.message = "Too low! Guess again!"
		else:
			self.message = "Too high! Guess again!"

		self.label_text.set(self.message)

	def reset(self):
		#self.entry.delete(0, END)
		self.secret_number = random.randint(1, 100)
		self.guess = 0
		self.num_guesses = 0

		self.message = "Guess a number from 1 to 100"
		self.label_text.set(self.message)

		self.guess_button.configure(state=NORMAL)
		self.reset_button.configure(state=DISABLED)

GUI(Tk()).start()
