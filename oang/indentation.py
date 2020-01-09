# import oang


class Indentation(object):
	def __init__(self, indent="\t"):
		self.indent = indent
		
		self.indentation_level = 0
		self.indentation_string = None
		self.indentation_length = None
		
	def set_indentation_level(self, indentation_level):
		if indentation_level != self.indentation_level:
			
			self.indentation_string = None
			self.indentation_level = indentation_level
			self.indentation_length = None
			
	def adjust_indentation_level(self, adjustment):
		self.set_indentation_level(self.indentation_level + adjustment)
		
	def reset_indentation_level(self):
		self.set_indentation_level(0)
		
	def increase_indentation_level(self):
		self.adjust_indentation_level(1)
		
	def decrease_indentation_level(self):
		self.adjust_indentation_level(-1)
		
	def get_indentation_level(self):
		return self.indentation_level
		
	def get_indentation_string(self):
		if self.indentation_string is None:
			self.indentation_string = self.indent * self.indentation_level
			
		return self.indentation_string
	
	def get_indentation_length(self):
		if self.indentation_length is None:
			self.indentation_length = len(self.get_indentation_string())
			
		return self.indentation_length