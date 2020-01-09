import lang


class Component_Sequence_Phrase(lang.Component_Sequence):
	__slots__ = [
		"phrase_definition"
	]
	
	def __init__(self, phrase_definition):
		super(Component_Sequence_Phrase, self).__init__(phrase_definition)
		
		self.phrase_definition = phrase_definition