import lang

import enumerable
import cact


class Interpreter_CallMethod(lang.Interpreter):
	__slots__ = [
		"method",
		"parameters"
	]
	
	def __init__(self, method, parameters=None):
		super(Interpreter_CallMethod, self).__init__()
		
		self.method = method
		self.parameters = cact.default_list(parameters)
		
	def interpret_parameters(self, environment, component):
		arguments = []
		
		for parameter in self.parameters:
			if isinstance(parameter, lang.ComponentDefinition):
				child_component = enumerable.new(component.get_children()) \
					.find(lambda c: c.component_definition == parameter)
					
				arguments.append(child_component.interpret(environment))
			else:
				arguments.append(parameter)
				
		return arguments