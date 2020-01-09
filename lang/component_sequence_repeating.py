import lang


class Component_Sequence_Repeating(lang.Component_Sequence):
	__slots__ = [
		"repeating_definition"
	]
	
	def __init__(self, repeating_definition):
		super(Component_Sequence_Repeating, self).__init__(repeating_definition)
		
		self.repeating_definition = repeating_definition