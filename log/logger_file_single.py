import log

import filex


class Logger_FileSingle(log.Logger):
	def __init__(self, filename):
		super(Logger_FileSingle, self).__init__()
		
		self.file = filex.fetch_file(filename, "Direct", "Direct")
		self.file.clear()
		
	def clear_internal(self):
		self.file.clear()
		
	def log_message_internal(self, message):
		self.file.set_text(message)