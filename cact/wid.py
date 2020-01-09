#import cact


class Wid(object):
	def __init__(self, **kwargs):
		self.values = kwargs
		self.is_dirty = True
		
	def update(self, **kwargs):
		for name, value in kwargs.iteritems():
			old_value = self.values[name]
			
			if value != old_value:
				self.values[name] = value
				self.is_dirty = True
				
		return self.is_dirty
				
	def validate(self):
		if self.is_dirty:
			self.commit()
			return True
		
		return False
				
	def commit(self):
		self.is_dirty = False