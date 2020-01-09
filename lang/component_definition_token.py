import lang


class ComponentDefinition_Token(lang.ComponentDefinition):
	__slots__ = [
		"token_definition"
	]
	
	def __init__(self, name, language):
		super(ComponentDefinition_Token, self).__init__(name, language)
	
	def create_component(self):
		return lang.Component_Token(self)
	
	def create_token(self, contents):
		return lang.Token(self, contents)
		
	def initilize(self, token_definition, interpreter=None):
		self.token_definition = token_definition
		self.initilize_interpreter(interpreter)
		return self
	
	def get_pattern(self):
		return self.token_definition.get_pattern()