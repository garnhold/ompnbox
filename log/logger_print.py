import log


class Logger_Print(log.Logger):
	def __init__(self):
		super(Logger_Print, self).__init__()
		
	def clear_internal(self):
		pass	
		
	def log_message_internal(self, message):
		print message