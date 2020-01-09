import log

import filex


class Logger_File(log.Logger):
	def __init__(self, filename):
		super(Logger_File, self).__init__()
		
		self.file = filex.fetch_file(filename, "Direct", "Direct")
		self.file.clear()
		
	def clear_internal(self):
		self.file.clear()
		
	def log_message_internal(self, message):
		self.file.append_text(message)