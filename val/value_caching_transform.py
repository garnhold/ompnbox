import val


class Value_Caching_Transform(val.Value_Caching):
	def __init__(self, value, operation):
		super(Value_Caching_Transform, self).__init__(lambda: operation(value.get_value()))
		
		self.value = value
		self.value_value = None
	
	def get_value(self):
		new_value = self.value.get_value()
		
		try:
			return self.fetch_value(new_value != self.value_value)
		finally:
			self.value_value = new_value