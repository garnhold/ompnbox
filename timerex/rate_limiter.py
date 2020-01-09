import timerex


class RateLimiter(object):
	def __init__(self, duration):
		self.timer = timerex.Timer_Duration(duration, True, True)
		
	def do_limit(self):
		if self.timer.is_time_up():
			self.timer.restart()
			return True
		
		return False