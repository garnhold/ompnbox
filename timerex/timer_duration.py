import timerex

import mhat


class Timer_Duration(timerex.Timer):
	def __init__(self, duration=1.0, start=False, expire=False):
		super(Timer_Duration, self).__init__(start)
		
		self.duration = duration
		
		if expire:
			self.expire()
		
	def expire(self):
		self.set_elapsed_time(self.duration)
		
	def set_duration(self, duration):
		self.duration = duration
		
	def get_duration(self):
		return self.duration
		
	def get_time_remaining(self):
		return mhat.bind_above(self.duration - self.get_elapsed_time(), 0.0)
		
	def is_time_up(self):
		if self.get_time_remaining() <= 0.0:
			return True
			
		return False
