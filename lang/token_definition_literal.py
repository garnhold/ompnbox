import lang

import flect
import re


class TokenDefinition_Literal(lang.TokenDefinition):
	__slots__ = [
		"literal"
	]
	
	def __init__(self, literal):
		super(TokenDefinition_Literal, self).__init__()
		
		self.literal = literal
	
	def get_pattern(self):
		return re.escape(self.literal)
	
	def __str__(self, *args, **kwargs):
		return self.literal
	
	def __repr__(self, *args, **kwargs):
		return flect.repr_self(self)