#import log

import oang
import traceback


class Logger(object):
	def __init__(self):
		self.indentation = oang.Indentation()
		
	def clear_internal(self):
		pass
		
	def log_message_internal(self, message):
		pass
		
	def clear(self):
		self.clear_internal()
		self.indentation.reset_indentation_level()
		
	def indent(self):
		self.indentation.increase_indentation_level()
		
	def dedent(self):
		self.indentation.decrease_indentation_level()
		
	def log_message(self, message):
		self.log_message_internal("> " + self.indentation.get_indentation_string() + str(message) + "\n")
		
	def log_error(self, message):
		self.log_message("ERROR: " + message);
	
	def log_exception(self):
		self.log_message(traceback.format_exc())