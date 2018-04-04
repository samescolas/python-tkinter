import json
import os

class Config():
	def __init__(self):
		if os.path.isfile('./config.json'):
			with open('./config.json', 'r') as fd:
				c = json.loads(fd.read())
				fd.close()
		else:
			c = {}

		self.TITLE = c['TITLE'] if 'TITLE' in c else 'tk'
		self.PROG_NAME = c['PROG_NAME'] if 'PROG_NAME' in c else 'Program'
