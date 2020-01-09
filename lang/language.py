import lang


class Language(object):
	__slots__ = [
		"tokenizer"
	]
	
	def __init__(self):
		self.tokenizer = lang.Tokenizer()
		
	def tokenize(self, text):
		return self.tokenizer.tokenize(text)
	
	def create_phrase(self, name):
		return lang.ComponentDefinition_Sequence_Phrase(name, self)
	
	def create_any(self, name):
		return lang.ComponentDefinition_Any(name, self)
	
	def create_repeating(self, name):
		return lang.ComponentDefinition_Sequence_Repeating(name, self)
	
	def create_interleaved(self, name):
		return lang.ComponentDefinition_Sequence_Interleaved(name, self)
	
	def make_token(self, name, component_definition_token, interpreter=None):
		return self.tokenizer.add_component_definition_token(lang.ComponentDefinition_Token(name, self).initilize(component_definition_token, interpreter))
	
	def make_token_ignore(self, name, component_definition_token, interpreter=None):
		return self.tokenizer.add_component_definition_token(lang.ComponentDefinition_Token_Ignore(name, self).initilize(component_definition_token, interpreter))