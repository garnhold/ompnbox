import log

import timerex


class Logger_Reducer(log.Logger):
	def __init__(self, logger, dump_interval=10.0):
		super(Logger_Reducer, self).__init__()
		
		self.logger = logger
		self.dump_rate_limiter = timerex.RateLimiter(dump_interval)
		self.recent_messages = []
		
	def clear_internal(self):
		self.logger.clear()
		
	def log_message_internal(self, message):
		if self.dump_rate_limiter.do_limit():
			self.recent_messages = []
		
		if message not in self.recent_messages:
			self.recent_messages.append(message)
			self.logger.log_message_internal(message)