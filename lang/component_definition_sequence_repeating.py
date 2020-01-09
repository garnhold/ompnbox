import lang


class ComponentDefinition_Sequence_Repeating(lang.ComponentDefinition_Sequence):
	__slots__ = [
		"component_definition",
		"min_occurances",
		"max_occurances"
	]
	
	def __init__(self, name, language):
		super(ComponentDefinition_Sequence_Repeating, self).__init__(name, language)
	
	def check_need_stop(self, components):
		number_components = len(components)
		
		if self.max_occurances is not None:
			if number_components >= self.max_occurances:
				return True
		
		return False
	
	def check_can_stop(self, components):
		number_components = len(components)
		
		if self.min_occurances is None or number_components >= self.min_occurances:
			return True
		
		return False
		
	def create_next_component(self, components):
		return self.component_definition.create_component()
		
	def create_component(self):
		return lang.Component_Sequence_Repeating(self)
	
	def initilize(self, component_definition, min_occurances=None, max_occurances=None, interpreter=None):
		self.component_definition = component_definition
		self.min_occurances = min_occurances
		self.max_occurances = max_occurances
		self.initilize_interpreter(interpreter)
		return self