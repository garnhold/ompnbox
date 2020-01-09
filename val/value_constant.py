import val


class Value_Constant(val.Value):
	def __init__(self, constant):
		self.constant = constant
	
	def get_value(self):
		return self.constant