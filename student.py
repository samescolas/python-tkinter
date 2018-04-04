class Student:
	def __init__(self, data):
		self.id = str(int(data[0].value))
		self.name_unicode = data[1].value
		self.name = data[1].value.encode('utf-8').strip()
		self.dept = data[2].value
		self.section = data[3].value
		self.fname = ' '.join(self.name.split(' ')[:-1])
		self.lname = self.name.split(' ')[-1]

	def comparison(self):
		# used to sort list based on last name first
		return self.lname + self.fname

	def __str__(self):
		return "{}, {}, {}".format(self.lname, self.fname, str(self.id))
