#import algae


class Variable(object):
	def __init__(self, name):
		self.name = name
		
	def __str__(self, *args, **kwargs):
		return self.name