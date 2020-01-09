import lang


class Interpreter_CallMethod_Static(lang.Interpreter_CallMethod):
	__slots__ = []
	
	def __init__(self, method, parameters=None):
		super(Interpreter_CallMethod_Static, self).__init__(method, parameters)
		
	def interpret(self, environment, component):
		return self.method(*self.interpret_parameters(environment, component))