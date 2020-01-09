import val

import timerex


class Value_Caching_Periodic(val.Value_Caching):
	def __init__(self, operation, duration):
		super(Value_Caching_Periodic, self).__init__(operation)
		
		self.rate_limiter = timerex.RateLimiter(duration)
		
	def get_value(self):
		return self.fetch_value(self.rate_limiter.do_limit())