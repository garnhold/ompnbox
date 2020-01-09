import filex


class FileWriteProvider(object):
	def __init__(self, filename):
		self.filename = filename
		
	def delete(self):
		filex.delete_internal(self.filename)
		
	def set_text(self, text):
		pass
	
	def append_text(self, text):
		pass
	
	def set_binary(self, binary):
		pass