import lang


class ComponentDefinition_Token_Ignore(lang.ComponentDefinition_Token):
	__slots__ = []
	
	def __init__(self, name, language):
		super(ComponentDefinition_Token_Ignore, self).__init__(name, language)
	
	def create_token(self, contents):
		return None