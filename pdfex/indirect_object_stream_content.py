import pdfex

import enumerable
import cact


class IndirectObject_Stream_Content(pdfex.IndirectObject_Stream):
	def __init__(self, statements=None):
		super(IndirectObject_Stream_Content, self).__init__(stream_filter_name="None")
		
		self.statements = cact.default_list(statements)
		
	def get_data(self):
		content_renderer = pdfex.ContentRenderer()
		
		content_renderer.start_section()
		
		for statement in self.statements:
			statement.render(content_renderer)
		
		content_renderer.end_section()
		
		return content_renderer.render()
	
	def get_xobjects(self):
		return enumerable.new(self.statements) \
			.expand(lambda s: s.get_xobjects())