import os
from tkinter import Tk, Button, Frame, Label, PhotoImage, LEFT
from config import Config

class App(Frame):
	def __init__(self,root=None):
		Frame.__init__(self,root)
		self.root = root
		self.conf = Config()
		self.render_title()
		self.render_header()
		self.render_filepicker()

	def render_title(self):
		self.root.title(self.conf.TITLE)
		#icon = PhotoImage(file=os.path.join(os.getcwd(), 'icon_8_24x24x32.png'))
		#self.root.tk.call('wm', 'iconphoto', self.root._w, icon)

	def render_header(self):
		header = Label(self.root, text=self.conf.PROG_NAME, font=('Arial', 30))
		header.pack()
		#header.grid(row=1, column=1)

	def render_filepicker(self):
		label = Label(self.root, text="Select student list Excel file:")
		button = Button(self.root, command=self.select_list, text="Import List")
		label.pack()
		button.pack()
		#label.grid(row=2, column=0)
		#button.grid(row=2, column=1)

	def select_list(event):
		print("SELECT LIST")


root = Tk()
app = App(root)
root.mainloop()
