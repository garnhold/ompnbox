import lang

import re
import flect


class TokenDefinition_Pattern(lang.TokenDefinition):
	__slots__ = [
		"regex"
	]
	
	def __init__(self, pattern):
		super(TokenDefinition_Pattern, self).__init__()
		
		self.regex = re.compile(pattern)
	
	def get_pattern(self):
		return self.regex.pattern
	
	def __str__(self, *args, **kwargs):
		return self.regex.pattern
	
	def __repr__(self, *args, **kwargs):
		return flect.repr_self(self)