import pdfex

import enumerable
import cact


class Statement_Compound(pdfex.Statement):
	def __init__(self, statements=None):
		super(Statement_Compound, self).__init__()
		
		self.statements = cact.default_list(statements)
	
	def render(self, content_renderer):
		for statement in self.statements:
			statement.render(content_renderer)
		
	def get_xobjects(self):
		return enumerable.new(self.statements) \
			.expand(lambda s: s.get_xobjects())