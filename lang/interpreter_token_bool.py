import lang

import flect


class Interpreter_Token_Bool(lang.Interpreter_Token):
	__slots__ = []
	
	def __init__(self):
		super(Interpreter_Token_Bool, self).__init__()
		
	def interpret_text(self, text):
		return flect.decode_bool_literal(text) 