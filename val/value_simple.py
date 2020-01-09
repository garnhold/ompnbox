import val


class Value_Simple(val.Value):
	def __init__(self, operation):
		self.operation = operation
	
	def get_value(self):
		return self.operation()