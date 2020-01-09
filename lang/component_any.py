import lang

import flect


class Component_Any(lang.Component):
	__slots__ = [
		"any_definition",
		"component"
	]
	
	def __init__(self, any_definition):
		super(Component_Any, self).__init__(any_definition)
		
		self.any_definition = any_definition
		
		self.component = None
		
	def initilize(self, tokens, index=0):
		highest_consumed = -1
		highest_consumed_component = None
		
		for component_definition in self.any_definition.component_definitions:
			component = component_definition.create_component()
			
			consumed = component.initilize(tokens, index)
			if consumed > highest_consumed:
				highest_consumed = consumed
				highest_consumed_component = component
			
		self.component = highest_consumed_component
		return highest_consumed
	
	def interpret(self, environment):
		return self.component.interpret(environment)
	
	def __str__(self, *args, **kwargs):
		return str(self.component)
	
	def __repr__(self, *args, **kwargs):
		return flect.repr_self_and_values(self, [self.any_definition])