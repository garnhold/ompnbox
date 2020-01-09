import algae


class Expression_Variable(algae.Expression):
	def __init__(self, variable):
		super(Expression_Variable, self).__init__()
		
		self.variable = variable
		
	def is_variable(self, variable):
		if variable == self.variable:
			return True
		
		return False
	
	def has_variable(self, variable):
		return self.is_variable(variable)
	
	def __str__(self, *args, **kwargs):
		return str(self.variable)