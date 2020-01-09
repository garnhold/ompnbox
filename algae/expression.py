#import algae


class Expression(object):
	def __init__(self):
		pass
	
	def is_variable(self, variable):
		return False
	
	def has_variable(self, variable):
		return False
	
	def get_variable_expressions(self, variable):
		return []
	
	def get_isolation_partial_operation(self, expression):
		return None