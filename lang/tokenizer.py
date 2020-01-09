#import lang

import flect
import enumerable
import rexex
import cact


class Tokenizer(object):
	__slots__ = [
		"component_definition_tokens",
		"multi_pattern"
	]
	
	def __init__(self, component_definition_tokens=None):
		self.component_definition_tokens = cact.default_list(component_definition_tokens)
		
		self.multi_pattern = None
		
	def validate(self):
		if not self.multi_pattern:
			self.multi_pattern = rexex.MultiPattern(
				enumerable.new(self.component_definition_tokens) \
					.convert(lambda d: d.get_pattern()) \
					.lst()
			)
			
	def tokenize(self, text):
		self.validate()
		
		tokens = []
		
		for info in self.multi_pattern.match_all(text):
			token = self.component_definition_tokens[info[0]].create_token(info[1])
			if token:
				tokens.append(token)
				
		return tokens
	
	def add_component_definition_token(self, component_definition_token):
		self.component_definition_tokens.append(component_definition_token)
		self.multi_pattern = None
		
		return component_definition_token
	
	def __str__(self, *args, **kwargs):
		return str(self.component_definition_tokens)
	
	def __repr__(self, *args, **kwargs):
		return flect.repr_self(self)