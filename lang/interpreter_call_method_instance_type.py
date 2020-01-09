import lang


class Interpreter_CallMethod_InstanceType(lang.Interpreter_CallMethod):
	__slots__ = []
	
	def __init__(self, cls, parameters=None):
		super(Interpreter_CallMethod_InstanceType, self).__init__(cls, parameters)
		
	def interpret(self, environment, component):
		obj = self.method(*self.interpret_parameters(environment, component))
		
		for component in component.get_children():
			component.interpret(obj)
			
		return obj