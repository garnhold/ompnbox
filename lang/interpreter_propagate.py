import lang


class Interpreter_Propagate(lang.Interpreter):
	__slots__ = []
	
	def __init__(self):
		super(Interpreter_Propagate, self).__init__()
		
	def interpret(self, environment, component):
		value = None
		
		for child in component.get_children():
			value = child.interpret(environment)
			
		return value