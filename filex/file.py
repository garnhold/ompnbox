# import filex

import val
import jsonex


class File(object):
	def __init__(self, filename, read_provider, write_provider):
		self.filename = filename
		
		self.read_provider = read_provider
		self.write_provider = write_provider
		
		self.json = val.Value_Caching_Transform(
			val.Value_Simple(lambda: self.get_text()),
			lambda v: jsonex.deserialize(v)
		)
		
		self.lines = val.Value_Caching_Transform(
			val.Value_Simple(lambda: self.get_text()),
			lambda v: v.splitlines()
		)
	
	def clear(self):
		self.set_text("")
		
	def delete(self):
		self.write_provider.delete()
	
	def set_text(self, text):
		self.write_provider.set_text(text)
		
	def append_text(self, text):
		self.write_provider.append_text(text)
		
	def set_json(self, obj):
		self.set_text(jsonex.serialize(obj))
		
	def set_binary(self, binary):
		self.write_provider.set_binary(binary)
	
	def get_filename(self):
		return self.filename
	
	def is_present(self):
		return self.read_provider.is_present()
		
	def get_text(self):
		return self.read_provider.get_text()
	
	def get_json(self):
		return self.json.get_value()
	
	def get_lines(self):
		return self.lines.get_value()
	
	def get_binary(self):
		return self.read_provider.get_binary()
		
	def get_size(self):
		return self.read_provider.get_size()
	
	def get_create_time(self):
		return self.read_provider.get_create_time()
	
	def get_last_write_time(self):
		return self.read_provider.get_last_write_time()