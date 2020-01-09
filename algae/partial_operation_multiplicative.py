import algae

import cact


class PartialOperation_Multiplicative(algae.PartialOperation):
	def __init__(self, multiply_expressions=None, divide_expressions=None):
		super(PartialOperation_Multiplicative, self).__init__()
		
		self.multiply_expressions = cact.default_list(multiply_expressions)
		self.divide_expressions = cact.default_list(divide_expressions)
		
	def apply(self, expression):
		return algae.Expression_Multiplicative([expression] + self.multiply_expressions, self.divide_expressions)