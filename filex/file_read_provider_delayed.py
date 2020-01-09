import filex

import val


class FileReadProvider_Delayed(filex.FileReadProvider):
	def __init__(self, filename):
		super(FileReadProvider_Delayed, self).__init__(filename)
		
		self.text = val.Value_Caching_Periodic(lambda: filex.read_text_internal(self.filename), 0.15)
		self.binary = val.Value_Caching_Periodic(lambda: filex.read_binary_internal(self.filename), 0.15)
		
		self.is_file = val.Value_Caching_Periodic(lambda: filex.is_file_internal(self.filename), 0.15)
		self.size = val.Value_Caching_Periodic(lambda: filex.get_size_internal(self.filename), 0.15)
		self.create_time = val.Value_Caching_Periodic(lambda: filex.get_create_time_internal(self.filename), 0.15)
		self.last_write_time = val.Value_Caching_Periodic(lambda: filex.get_last_write_time_internal(self.filename), 0.15)
		
	def is_present(self):
		return self.is_file.get_value()
		
	def get_text(self):
		return self.text.get_value()
	
	def get_binary(self):
		return self.binary.get_value()
		
	def get_size(self):
		return self.size.get_value()
	
	def get_create_time(self):
		return self.create_time.get_value()
	
	def get_last_write_time(self):
		return self.last_write_time.get_value()