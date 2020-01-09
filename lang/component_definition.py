import lang

import flect


class ComponentDefinition(object):
	__slots__ = [
		"name",
		"language",
		"interpreter"
	]
	
	def __init__(self, name, language):
		self.name = name
		self.language = language
		
	def create_component(self):
		return None
	
	def initilize_interpreter(self, interpreter):
		if interpreter:
			self.interpreter = interpreter
		else:
			self.interpreter = lang.Interpreter_Propagate()
			
	def interpret(self, environment, component):
		return self.interpreter.interpret(environment, component)
	
	def parse_tokens(self, tokens):
		component = self.create_component()
		
		consumed = component.initilize(tokens)
		if consumed == len(tokens):
			return component.interpret(None)
	
	def parse_text(self, text):
		return self.parse_tokens(self.language.tokenize(text))
	
	def __str__(self, *args, **kwargs):
		return self.name
	
	def __repr__(self, *args, **kwargs):
		return flect.repr_self(self)