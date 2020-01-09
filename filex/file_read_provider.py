# import filex


class FileReadProvider(object):
	def __init__(self, filename):
		self.filename = filename
		
	def is_present(self):
		pass
		
	def get_text(self):
		pass
	
	def get_binary(self):
		pass
		
	def get_size(self):
		pass
	
	def get_create_time(self):
		pass
	
	def get_last_write_time(self):
		pass