import val


class Value_Caching(val.Value):
	def __init__(self, operation):
		super(Value_Caching, self).__init__()
		
		self.cached_value = None
		self.is_cached = False
		
		self.operation = operation
	
	def fetch_value(self, clear_cache):
		if clear_cache or not self.is_cached:
			self.cached_value = self.operation()
			self.is_cached = True
			
		return self.cached_value