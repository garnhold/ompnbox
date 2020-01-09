import log

import filex


class Logger_PassFile(log.Logger):
	def __init__(self, filename):
		super(Logger_PassFile, self).__init__()
		
		self.buffer = ""
		self.file = filex.fetch_file(filename)
		self.file.clear()
		
	def clear_internal(self):
		self.buffer = ""
		
	def log_message_internal(self, message):
		self.buffer += message
	
	def dump(self):
		self.file.set_text(self.buffer)
		self.buffer = ""