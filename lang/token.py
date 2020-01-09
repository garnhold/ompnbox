# import lang

import flect


class Token(object):
	__slots__ = [
		"token_definition",
		"contents"
	]
	
	def __init__(self, token_definition, contents):
		self.token_definition = token_definition
		self.contents = contents
		
	def __str__(self, *args, **kwargs):
		return str(self.contents)
		
	def __repr__(self, *args, **kwargs):
		return flect.repr_self(self)