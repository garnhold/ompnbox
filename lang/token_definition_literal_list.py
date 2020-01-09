import lang

import flect
import rexex


class TokenDefinition_LiteralList(lang.TokenDefinition):
	__slots__ = [
		"literals"
	]
	
	def __init__(self, literals):
		super(TokenDefinition_LiteralList, self).__init__()
		
		self.literals = literals
	
	def get_pattern(self):
		return rexex.alternative_strings_group(self.literals)
	
	def __str__(self, *args, **kwargs):
		return str(self.literals)
	
	def __repr__(self, *args, **kwargs):
		return flect.repr_self(self)