import lang

import flect


class Interpreter_Token_QuotedString(lang.Interpreter_Token):
	__slots__ = []
	
	def __init__(self):
		super(Interpreter_Token_QuotedString, self).__init__()
		
	def interpret_text(self, text):
		return flect.decode_string_literal(text)