import pdfex


class Entry_Constant(pdfex.Entry):
	def __init__(self, name, value):
		super(Entry_Constant, self).__init__(name)
		
		self.value = value
		
	def get_value(self):
		return self.value