import lang


class Component_Sequence_Interleaved(lang.Component_Sequence):
	__slots__ = [
		"interleaved_definition"
	]
	
	def __init__(self, interleaved_definition):
		super(Component_Sequence_Interleaved, self).__init__(interleaved_definition)
		
		self.interleaved_definition = interleaved_definition