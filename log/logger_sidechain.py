import log


class Logger_Sidechain(log.Logger):
	def __init__(self, label, logger):
		super(Logger_Sidechain, self).__init__()
		
		self.label = label
		self.logger = logger
		
	def clear_internal(self):
		self.logger.clear()
		
	def log_message_internal(self, message):
		self.logger.log_message_internal(message)
		log.get_logger().log_message_internal(self.label + " : " + message)