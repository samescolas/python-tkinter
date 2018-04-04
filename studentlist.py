import xlrd
from student import Student

class Studentlist:
	def __init__(self, path):
		self.path = path
		self.students = []
		self.load()
	
	def load(self):
		try:
			sheet = xlrd.open_workbook(self.path).sheet_by_index(0)
			for i in range(1,sheet.nrows):
				self.students.append(Student(sheet.row(i)))
			self.students.sort(key=Student.comparison)
			self.sections = list(set([s.section for s in self.students]))
		except:
			raise BaseException('Spreadsheet format unrecognized.')

	def __str__(self):
		return "\n".join([str(s) for s in self.students])
	
	def __len__(self):
		return len(self.students)
