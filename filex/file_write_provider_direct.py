import filex


class FileWriteProvider_Direct(filex.FileWriteProvider):
	def __init__(self, filename):
		super(FileWriteProvider_Direct, self).__init__(filename)
		
	def set_text(self, text):
		filex.write_text_internal(self.filename, text)
		
	def append_text(self, text):
		filex.append_text_internal(self.filename, text)
		
	def set_binary(self, binary):
		filex.write_binary_internal(self.filename, binary)