#import lect


class Palette(object):
	__SLOTS__ = [
		"index_to_value",
		"value_to_index"
	]
	
	def __init__(self, values=None):
		self.index_to_value = []
		self.value_to_index = {}
		
		if values:
			self.update(values)
		
	def add(self, value):
		self.index_to_value.append(value)
		self.value_to_index[value] = len(self.index_to_value) - 1
		
	def update(self, values):
		for value in values:
			self.add(value)
			
	def get_index(self, value, default_index=None):
		return self.value_to_index.get(value, default_index)
			
	def get_value(self, index, default_value=None):
		if index < len(self.index_to_value):
			return self.index_to_value[index]
		
		return default_value
			
	def __iter__(self):
		return iter(self.index_to_value)
			
	def indexs(self):
		return range(0, len(self.index_to_value))
	
	def values(self):
		return self.index_to_value
			
	def iteritems(self):
		for i in range(0, len(self.index_to_value)):
			yield i, self.index_to_value[i]