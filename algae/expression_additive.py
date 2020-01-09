import algae

import cact
import enumerable


class Expression_Additive(algae.Expression):
	def __init__(self, add_expressions=None, subtract_expressions=None):
		super(Expression_Additive, self).__init__()
		
		self.add_expressions = cact.default_list(add_expressions)
		self.subtract_expressions = cact.default_list(subtract_expressions)
		
	def has_variable(self, variable):
		return enumerable.new(self.add_expressions) \
			.append(self.subtract_expressions) \
			.has(lambda e: e.has_variable(variable))
		
	def get_variable_expressions(self, variable):
		return enumerable.new(self.add_expressions) \
			.append(self.subtract_expressions) \
			.narrow(lambda e: e.has_variable(variable)) \
			.lst()
			
	def get_isolation_partial_operation(self, expression):
		return algae.PartialOperation_Additive(
			enumerable.new(self.subtract_expressions)
				.skip_item(expression)
				.lst(),
				
			enumerable.new(self.add_expressions) 
				.skip_item(expression)
				.lst()
		)
		
	def __str__(self, *args, **kwargs):
		return "(" + \
			"(" + enumerable.new(self.add_expressions).str(" + ") + ")" \
			"- (" + enumerable.new(self.subtract_expressions).str(" + ") + ")" \
		")"