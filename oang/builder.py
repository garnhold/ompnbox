#import oang


class Builder(object):
	def __init__(self):
		self.length = 0
		self.strings = []
	
	def clear(self):
		self.length = 0
		self.strings = []
		
	def append(self, string):
		if string:
			self.length += len(string)
			self.strings.append(string)
		
	def render(self):
		return "".join(self.strings)
	
	def get_length(self):
		return self.length
	
	def __str__(self, *args, **kwargs):
		return self.render()
	
	def __len__(self):
		return self.get_length()