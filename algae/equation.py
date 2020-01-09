#import algae


class Equation(object):
	def __init__(self, left_expression=None, right_expression=None):
		self.left_expression = left_expression
		self.right_expression = right_expression
		
	def solve_for_variable(self, variable):
		left_has_variable = self.left_expression.has_variable(variable)
		right_has_variable = self.right_expression.has_variable(variable)
		
		target_expression = None
		reduction_expression = None
		
		if left_has_variable and not right_has_variable:
			target_expression = self.left_expression
			reduction_expression = self.right_expression
			
		if right_has_variable and not left_has_variable:
			target_expression = self.right_expression
			reduction_expression = self.left_expression
			
		if target_expression and reduction_expression:
			while target_expression.is_variable(variable) == False:
				expressions = target_expression.get_variable_expressions(variable)
				
				if len(expressions) > 1:
					return None
				
				sub_expression = expressions[0]
				reduction_expression = target_expression \
					.get_isolation_partial_operation(sub_expression) \
					.apply(reduction_expression)
					
				target_expression = sub_expression
					
		return reduction_expression
	
	def __str__(self, *args, **kwargs):
		return str(self.left_expression) + " = " + str(self.right_expression)