import filex


class FileWriteProvider_Buffered(filex.FileWriteProvider):
	def __init__(self, filename):
		super(FileWriteProvider_Buffered, self).__init__(filename)
		
		self.text = None
		self.binary = None
		
	def set_text(self, text):
		if text != self.text:
			self.text = text
			self.binary = None
			
			filex.write_text_internal(self.filename, self.text)
			
	def append_text(self, text):
		filex.append_text_internal(self.filename, text)
		
	def set_binary(self, binary):
		if binary != self.binary:
			self.text = None
			self.binary = binary
			
			filex.write_binary_internal(self.filename, self.binary)