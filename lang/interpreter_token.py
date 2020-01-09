import lang


class Interpreter_Token(lang.Interpreter):
	__slots__ = []
	
	def __init__(self):
		super(Interpreter_Token, self).__init__()
		
	def interpret_text(self, text):
		return None
		
	def interpret(self, environment, component):
		if isinstance(component, lang.Component_Token):
			return self.interpret_text(component.token.contents)
		
		return self.interpret_text("")