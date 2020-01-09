import huva


class UnitDefinition_Internal(huva.UnitDefinition):
	def __init__(self, singular_name, plural_name, abbreviations):
		super(UnitDefinition_Internal, self).__init__(singular_name, plural_name, abbreviations)
		
	def convert_to_internal(self, value, world=0.0):
		return value
	
	def convert_from_internal(self, value, world=0.0):
		return value