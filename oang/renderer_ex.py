import oang

import re


class RendererEX(oang.Renderer):
	def __init__(self, value_render_providers, indent_character="\t", newline_character="\n"):
		super(RendererEX, self).__init__(indent_character, newline_character)
		
		self.value_renderer = oang.ValueRenderer(value_render_providers)
	
	def append_format(self, text, *args):
		final_index  = 0
		
		for match in re.finditer("(.*?)\\{([0-9]+)\\}", text):
			self.append(match.group(1))
			self.append_value(args[int(match.group(2))])
			
			final_index = match.end()
			
		self.append(text[final_index:])
		
	def append_line_format(self, text, *args):
		self.start_line()
		self.append_format(text, *args)
		self.end_line()
		
	def append_value(self, value):
		self.value_renderer.render(self, value)
		
	def append_value_get_offset(self, value):
		offset = self.get_length()
		self.append_value(value)
		
		return offset
		
	def append_line_value(self, value):
		self.start_line()
		self.append_value(value)
		self.end_line()
		
	def append_line_value_get_offset(self, value):
		self.start_line()
		offset = self.append_value_get_offset(value)
		self.end_line()
		
		return offset