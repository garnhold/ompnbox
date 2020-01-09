import lang


class ComponentDefinition_Sequence_Phrase(lang.ComponentDefinition_Sequence):
	__slots__ = [
		"component_definitions"
	]
	
	def __init__(self, name, language):
		super(ComponentDefinition_Sequence_Phrase, self).__init__(name, language)
	
	def create_component(self):
		return lang.Component_Sequence_Phrase(self)
	
	def check_need_stop(self, components):
		if len(components) >= len(self.component_definitions):
			return True
		
		return False
	
	def check_can_stop(self, components):
		False	
	
	def create_next_component(self, components):
		return self.component_definitions[len(components)].create_component()
	
	def initilize(self, component_definitions, interpreter=None):
		self.component_definitions = component_definitions
		self.initilize_interpreter(interpreter)
		return self