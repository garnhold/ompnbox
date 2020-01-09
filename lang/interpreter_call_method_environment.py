import lang


class Interpreter_CallMethod_Environment(lang.Interpreter_CallMethod):
	__slots__ = []
	
	def __init__(self, method, parameters=None):
		super(Interpreter_CallMethod_Environment, self).__init__(method, parameters)
		
	def interpret(self, environment, component):
		return self.method(environment, *self.interpret_parameters(environment, component))