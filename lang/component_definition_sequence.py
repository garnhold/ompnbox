import lang


class ComponentDefinition_Sequence(lang.ComponentDefinition):
	__slots__ = []
	
	def __init__(self, name, language):
		super(ComponentDefinition_Sequence, self).__init__(name, language)
	
	def check_need_stop(self, components):
		return False
	
	def check_can_stop(self, components):
		return False
		
	def create_next_component(self, components):
		return None