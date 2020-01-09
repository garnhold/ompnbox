import lang

import enumerable
import flect


class Component_Sequence(lang.Component):
	__slots__ = [
		"sequence_definition",
		"components"
	]
	
	def __init__(self, sequence_definition):
		super(Component_Sequence, self).__init__(sequence_definition)
		
		self.sequence_definition = sequence_definition
		
		self.components = []
		
	def initilize(self, tokens, index=0):
		total_consumed = 0
		
		while self.sequence_definition.check_need_stop(self.components) == False:
			component = self.sequence_definition.create_next_component(self.components)
			
			consumed = component.initilize(tokens, index)
			if consumed == -1:
				if self.sequence_definition.check_can_stop(self.components):
					return total_consumed
				
				return -1
			
			index += consumed
			total_consumed += consumed
			self.components.append(component)
			
		return total_consumed
	
	def get_children(self):
		return self.components
	
	def __str__(self, *args, **kwargs):
		return "[" + enumerable.new(self.components).str(", ") + "]"
	
	def __repr__(self, *args, **kwargs):
		return flect.repr_self_and_values(self, [self.sequence_definition])