import pdfex

import enumerable
import cact


class Statement_GraphicsStateBlock(pdfex.Statement):
	def __init__(self, statements=None):
		super(Statement_GraphicsStateBlock, self).__init__()
		
		self.statements = cact.default_list(statements)
	
	def render(self, content_renderer):
		content_renderer.append_line("q")
		content_renderer.start_section()
		
		for statement in self.statements:
			statement.render(content_renderer)
		
		content_renderer.end_section()
		content_renderer.append_line("Q")
		
	def get_xobjects(self):
		return enumerable.new(self.statements) \
			.expand(lambda s: s.get_xobjects())