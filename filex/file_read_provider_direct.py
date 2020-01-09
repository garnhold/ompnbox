import filex


class FileReadProvider_Direct(filex.FileReadProvider):
	def __init__(self, filename):
		self.filename = filename
		
	def is_present(self):
		return filex.is_file_internal(self.filename)
		
	def get_text(self):
		return filex.read_text_internal(self.filename)
	
	def get_binary(self):
		return filex.read_binary_internal(self.filename)
		
	def get_size(self):
		return filex.get_size_internal(self.filename)
	
	def get_create_time(self):
		return filex.get_create_time_internal(self.filename)
	
	def get_last_write_time(self):
		return filex.get_last_write_time_internal(self.filename)