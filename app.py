#!/usr/bin/python

from Tkinter import Tk, Label, Button, Listbox, Entry, StringVar, DISABLED, NORMAL, END, MULTIPLE, W, E, N, S
import tkFileDialog, ttk
import xlwt
from config import Config
from studentlist import Studentlist

class GUI:
	def __init__(self, master):
		self.master = master
		self.conf = Config()
		self.student_list = None
		self.save_filetype = StringVar()
		self.save_filetype.set('.txt')
		self.selected_section = StringVar()
		self.selected_section.set('ENGR 102 01')
		self.week = StringVar()
		self.week.set('42')
		self.student_listbox_contents = []
		self.attended_students = []

		# Set title
		master.title(self.conf.TITLE)

		# Header Label
		self.header_label_text = StringVar()
		self.header_label_text.set(self.conf.PROG_NAME)
		self.header_label = Label(master, textvariable=self.header_label_text, font=('Arial', 25))

		# File Import Label
		self.file_label_text = StringVar()
		self.file_label_text.set("Select student list Excel file:")
		self.file_label = Label(master, textvariable=self.file_label_text, font=('Arial', 15, 'bold'))

		# File Import Button
		self.file_button = Button(master, text="Import List", command=self.select_list)


		self.header_label.grid(row=0, column=1, columnspan=4, sticky=W+E)
		self.file_label.grid(row=1, column=0, columnspan=2, sticky=W)
		self.file_button.grid(row=1, column=2, columnspan=1, sticky=W+E)
		#self.reset_button.grid(row=3, column=1)

	def render_student_listbox(self):
		self.student_listbox_contents = []
		# Students Label
		self.student_label = Label(self.master, text="Select a Student:", font=('Arial', 15, 'bold'))

		# Students Listbox
		self.students_listbox = Listbox(self.master,
										selectmode=MULTIPLE,
										height=10)
		selected_section = self.selected_section.get()
		for i,s in enumerate(self.student_list.students):
			if s.section == selected_section:
				self.students_listbox.insert(i, str(s))
				self.student_listbox_contents.append(s)
		self.student_label.grid(row=2, column=0, columnspan=1, sticky=W)
		self.students_listbox.grid(row=3, rowspan=13, column=0, columnspan=2, sticky=W+E)

	def render_attended_students_listbox(self):
		# Attended Students Label
		self.attended_students_label = Label(self.master, text="Attended Students:", font=('Arial', 15, 'bold'))
		
		# Attended Students Listbox
		self.attended_students_listbox = Listbox(self.master,
												 selectmode=MULTIPLE,
												 height=10,
												 width=20)
		for i,s in enumerate(self.attended_students):
			self.attended_students_listbox.insert(i, str(s))
		self.attended_students_label.grid(row=2, column=3, sticky=W)
		self.attended_students_listbox.grid(row=3, rowspan=13, column=3, columnspan=7, sticky=W+E)
			

	def render_section_combobox(self):
		self.section_label = Label(self.master, text="Section:", font=('Arial', 15, 'bold'))
		self.section_combobox = ttk.Combobox(self.master,
											 height=len(self.student_list),
											 textvariable=self.selected_section,
											 values=self.student_list.sections)
		self.section_combobox.bind("<<ComboboxSelected>>", self.sectionchange)
		self.section_label.grid(row=2, column=2)
		self.section_combobox.grid(row=3, column=2, sticky=W+E+N+S)

	def render_add_remove(self):
		self.add_button = Button(self.master, text="Add ->", command=self.add_students)
		self.remove_button = Button(self.master, text="<- Remove", command=self.remove_students)

		self.add_button.grid(row=4, column=2, sticky=W+E+N+S)
		self.remove_button.grid(row=5, column=2, sticky=W+E+N+S)

	def render_export_section(self):
		self.filetype_label = Label(self.master, text="Please select file type:", font=('Arial', 13, 'bold'))
		self.filetype_combobox = ttk.Combobox(self.master,
											  height=3,
											  textvariable=self.save_filetype,
											  values=['.xls', '.csv', '.txt'])
		self.filetype_combobox.bind("<<ComboboxSelected>>", self.save_filetype_change)
		self.week_label = Label(self.master, text="Please enter week:", font=('Arial', 13, 'bold'))
		self.week_entry = Entry(self.master, textvariable=self.week)
		self.export_button = Button(self.master, text="Export as File", command=self.export_list)

		self.filetype_label.grid(row=18, column=0, sticky=W)
		self.filetype_combobox.grid(row=18, column=1, sticky=E)
		self.week_label.grid(row=18, column=2)
		self.week_entry.grid(row=18, column=3, sticky=W+E)
		self.export_button.grid(row=18, column=4, sticky=W+E)


	def start(self):
		self.master.mainloop()

	def add_students(self):
		ixs = self.students_listbox.curselection()
		for i in ixs:
			self.attended_students.append(self.student_listbox_contents[i])
		self.attended_students = list(set(self.attended_students))
		self.render_attended_students_listbox()
		self.students_listbox.selection_clear(0, END)

	def remove_students(self):
		ixs = list(self.attended_students_listbox.curselection())
		ixs.reverse()
		for i in ixs:
			del self.attended_students[i]
		self.render_attended_students_listbox()

	def export_list(self):
		save_filename = "{}{}{}".format(self.selected_section.get(), self.week.get(), self.save_filetype.get())
		if self.save_filetype.get() == '.txt':
			try:
				with open(save_filename, 'w') as fd:
					for i,s in enumerate(self.attended_students):
						fd.write("{}\t{}\t{}\n".format(s.id, s.name, s.dept))
				fd.close()
			except:
				print("Unable to open file.")
		elif self.save_filetype.get() == '.xls':
			book = xlwt.Workbook()
			sheet = book.add_sheet('Sheet 1')
			sheet.write(0, 0, 'Id')
			sheet.write(0, 1, 'Name')
			sheet.write(0, 2, 'Dept.')
			for i,s in enumerate(self.attended_students):
				sheet.write(i+1, 0, s.id)
				sheet.write(i+1, 1, s.name_unicode)
				sheet.write(i+1, 2, s.dept)
			book.save(save_filename)
		else:
			raise BaseException('Filetype is not supported.')

	def select_list(self):
		self.list_file = tkFileDialog.askopenfilename(initialdir="~",
													  title="Import List",
													  filetypes = (("Excel Files","*.xls*"),("all files","*.*")))
		if self.list_file:
			self.student_list = Studentlist(self.list_file)
			self.render_student_listbox()
			self.render_attended_students_listbox()
			self.render_section_combobox()
			self.render_add_remove()
			self.render_export_section()

	def sectionchange(self, event):
		self.selected_section.set(self.section_combobox.get())
		self.attended_students = []
		self.render_student_listbox()
		self.render_attended_students_listbox()

	def save_filetype_change(self, event):
		self.save_filetype.set(self.filetype_combobox.get())


GUI(Tk()).start()
