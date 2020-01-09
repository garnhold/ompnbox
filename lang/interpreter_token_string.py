import lang


class Interpreter_Token_String(lang.Interpreter_Token):
	__slots__ = []
	
	def __init__(self):
		super(Interpreter_Token_String, self).__init__()
		
	def interpret_text(self, text):
		return text