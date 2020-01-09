import oang


class Renderer(object):
	def __init__(self, indent_character="\t", newline_character="\n"):
		self.current_line = ""
		self.builder = oang.Builder()
		
		self.newline_character = newline_character
		self.indentation = oang.Indentation_Suspendable(indent_character)
		
	def clear(self):
		self.current_line = ""
		self.builder.clear()
		self.indentation.reset_indentation_level()
		
	def blank_line(self):
		self.end_line()
		self.builder.append(self.newline_character)
	
	def clear_line(self, text=""):
		self.current_line = text
		
	def start_line(self, text=""):
		self.end_line()
		self.current_line = text
		
	def end_line(self, text=None):	
		if self.current_line:
			if text:
				self.append(text)
			
			self.builder.append(self.render_current_line())
			self.builder.append(self.newline_character)
			
		self.current_line = ""
		
	def start_section(self):
		self.end_line()
		self.indentation.increase_indentation_level()
		self.start_line()
	
	def end_section(self):
		self.end_line()
		self.indentation.decrease_indentation_level()
		
	def suspend_indentation(self):
		self.end_line()
		self.indentation.suspend()
		
	def resume_indentation(self):
		self.end_line()
		self.indentation.resume()
		
	def append(self, text):
		self.current_line += text
		
	def append_get_offset(self, text):
		offset = self.get_length()
		self.append(text)
		
		return offset
		
	def append_line(self, text):
		self.start_line()
		self.append(text)
		self.end_line()
		
	def append_line_get_offset(self, text):
		self.start_line()
		offset = self.append_get_offset(text)
		self.end_line()
		
		return offset
		
	def render(self):
		return self.builder.render() + self.render_current_line()
	
	def render_current_line(self):
		if self.current_line:
			return self.indentation.get_indentation_string() + self.current_line
		
		return ""
	
	def get_length(self):
		return self.builder.get_length() + self.get_current_line_length()
	
	def get_current_line_length(self):
		if self.current_line:
			return self.indentation.get_indentation_length() + len(self.current_line)
		
		return 0
	
	def __str__(self, *args, **kwargs):
		return self.render()
	
	def __len__(self):
		return self.get_length()