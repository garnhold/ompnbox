import algae

import cact


class PartialOperation_Additive(algae.PartialOperation):
	def __init__(self, add_expressions=None, subtract_expressions=None):
		super(PartialOperation_Additive, self).__init__()
		
		self.add_expressions = cact.default_list(add_expressions)
		self.subtract_expressions = cact.default_list(subtract_expressions)
		
	def apply(self, expression):
		return algae.Expression_Additive([expression] + self.add_expressions, self.subtract_expressions)