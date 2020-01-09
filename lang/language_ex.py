import lang


class LanguageEX(lang.Language):
	__slots__ = []
	
	def __init__(self):
		super(LanguageEX, self).__init__()
		
	def make_literal_token(self, name, literal, interpreter=None):
		return self.make_token(name, lang.TokenDefinition_Literal(literal), interpreter)
	
	def make_literal_list_token(self, name, literals, interpreter=None):
		return self.make_token(name, lang.TokenDefinition_LiteralList(literals), interpreter)
	
	def make_pattern_token(self, name, pattern, interpreter=None):
		return self.make_token(name, lang.TokenDefinition_Pattern(pattern), interpreter)
	
	def make_literal_token_ignore(self, name, literal):
		return self.make_token_ignore(name, lang.TokenDefinition_Literal(literal))
	
	def make_literal_list_token_ignore(self, name, literals):
		return self.make_token_ignore(name, lang.TokenDefinition_LiteralList(literals))
	
	def make_pattern_token_ignore(self, name, pattern):
		return self.make_token_ignore(name, lang.TokenDefinition_Pattern(pattern))
	
	def make_expression(self, name, term, operands):
		i = 0
		
		for operand in operands:
			term = self.create_repeating(name + str(i)).initilize(term, operand)
			i += 1
			
		return term