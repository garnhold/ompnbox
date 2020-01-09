import pdfex


class Entry_Value(pdfex.Entry):
	def __init__(self, variable_name, name, value=None):
		super(Entry_Value, self).__init__(name)
		
		self.variable_name = variable_name
		self.value = value
		
	def set_value(self, value):
		self.value = value
		
	def get_value(self):
		return self.value