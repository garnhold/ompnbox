import lang

import enumerable


class ComponentDefinition_Sequence_Interleaved(lang.ComponentDefinition_Sequence):
	__slots__ = [
		"component_definition",
		"interleaving_definition",
		"min_occurances",
		"max_occurances"
	]
	
	def __init__(self, name, language):
		super(ComponentDefinition_Sequence_Interleaved, self).__init__(name, language)
		
	def calculate_final_component_definition(self, components):
		if len(components) <= 0:
			return None
		
		return components[-1].component_definition
	
	def calculate_number_full_components(self, components):
		return enumerable.count(components, lambda c: c.component_definition == self.component_definition)
		
	def check_need_stop(self, components):
		if self.max_occurances is not None:
			if self.calculate_final_component_definition(components) != self.interleaving_definition:
				if self.calculate_number_full_components(components) >= self.max_occurances:
					return True
		
		return False
	
	def check_can_stop(self, components):
		if self.calculate_final_component_definition(components) != self.interleaving_definition:
			if self.min_occurances is None or self.calculate_number_full_components(components) >= self.min_occurances:
				return True
		
		return False
		
	def create_next_component(self, components):
		if len(components) % 2 == 0:
			return self.component_definition.create_component()
		
		return self.interleaving_definition.create_component()
		
	def create_component(self):
		return lang.Component_Sequence_Interleaved(self)
	
	def initilize(self, component_definition, interleaving_definition, min_occurances=None, max_occurances=None, interpreter=None):
		self.component_definition = component_definition
		self.interleaving_definition = interleaving_definition
		self.min_occurances = min_occurances
		self.max_occurances = max_occurances
		self.initilize_interpreter(interpreter)
		return self