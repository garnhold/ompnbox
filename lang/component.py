# import lang

import flect


class Component(object):
	__slots__ = [
		"component_definition"
	]
	
	def __init__(self, component_definition):
		self.component_definition = component_definition
		
	def initilize(self, tokens, index=0):
		return -1
	
	def interpret(self, environment):
		return self.component_definition.interpret(environment, self)
	
	def get_children(self):
		return []
	
	def __str__(self, *args, **kwargs):
		return str(self.component_definition)
	
	def __repr__(self, *args, **kwargs):
		return flect.repr_self(self)