import lang


class ComponentDefinition_Any(lang.ComponentDefinition):
	__slots__ = [
		"component_definitions"
	]
	
	def __init__(self, name, language):
		super(ComponentDefinition_Any, self).__init__(name, language)
		
	def create_component(self):
		return lang.Component_Any(self)
	
	def initilize(self, component_definitions, interpreter=None):
		self.component_definitions = component_definitions
		self.initilize_interpreter(interpreter)
		return self