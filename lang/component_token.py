import lang

import flect


class Component_Token(lang.Component):
	__SLOTS__ = [
		"token",
		"token_definition"
	]
	
	def __init__(self, token_definition):
		super(Component_Token, self).__init__(token_definition)
		
		self.token = None
		self.token_definition = token_definition
		
	def initilize(self, tokens, index=0):
		if index < len(tokens):
			token = tokens[index]
			
			if token.token_definition == self.token_definition:
				self.token = token
				return 1
		
		return -1
	
	def __str__(self, *args, **kwargs):
		return str(self.token)
	
	def __repr__(self, *args, **kwargs):
		return flect.repr_values(self, [self.token_definition, self.token])