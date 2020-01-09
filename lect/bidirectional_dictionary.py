#import lect


class BidirectionalDictionary(object):
	__SLOTS__ = [
		"left_to_right",
		"right_to_left"
	]
	
	def __init__(self, values=None):
		self.left_to_right = {}
		self.right_to_left = {}
		
		if values:
			self.update(values)
		
	def add(self, left, right):
		self.left_to_right[left] = right
		self.right_to_left[right] = left
		
	def update(self, values):
		for left, right in values.iteritems():
			self.add(left, right)
			
	def get_by_left(self, left, default_value=None):
		return self.left_to_right.get(left, default_value)
	get_right = get_by_left
	
	def get_by_right(self, right, default_value=None):
		return self.right_to_left.get(right, default_value)
	get_left = get_by_right
			
	def __iter__(self):
		return iter(self.left_to_right)
			
	def lefts(self):
		return self.left_to_right.keys()
	
	def rights(self):
		return self.right_to_left.keys()
			
	def iteritems(self):
		return self.left_to_right.iteritems()