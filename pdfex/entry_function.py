import pdfex


class Entry_Function(pdfex.Entry):
	def __init__(self, name, function):
		super(Entry_Function, self).__init__(name)
		
		self.function = function
		
	def get_value(self):
		return self.function()