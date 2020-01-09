import algae

import cact
import enumerable


class Expression_Multiplicative(algae.Expression):
	def __init__(self, multiply_expressions=None, divide_expressions=None):
		super(Expression_Multiplicative, self).__init__()
		
		self.multiply_expressions = cact.default_list(multiply_expressions)
		self.divide_expressions = cact.default_list(divide_expressions)
	
	def has_variable(self, variable):
		return enumerable.new(self.multiply_expressions) \
			.append(self.divide_expressions) \
			.has(lambda e: e.has_variable(variable))
		
	def get_variable_expressions(self, variable):
		return enumerable.new(self.multiply_expressions) \
			.append(self.divide_expressions) \
			.narrow(lambda e: e.has_variable(variable)) \
			.lst()
			
	def get_isolation_partial_operation(self, expression):
		return algae.PartialOperation_Multiplicative(
			enumerable.new(self.divide_expressions)
				.skip_item(expression)
				.lst(),
				
			enumerable.new(self.multiply_expressions)
				.skip_item(expression)
				.lst()
		)
		
	def __str__(self, *args, **kwargs):
		return "(" + \
			"(" + enumerable.new(self.multiply_expressions).str(" * ") + ")" \
			"/ (" + enumerable.new(self.divide_expressions).str(" * ") + ")" \
		")"