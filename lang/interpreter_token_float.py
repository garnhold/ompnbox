import lang


class Interpreter_Token_Float(lang.Interpreter_Token):
	__slots__ = []
	
	def __init__(self):
		super(Interpreter_Token_Float, self).__init__()
		
	def interpret_text(self, text):
		return float(text)