import huva


class UnitDefinition_ThisIsNThat(huva.UnitDefinition):
	def __init__(self, singular_name, plural_name, abbreviations, n, that):
		super(UnitDefinition_ThisIsNThat, self).__init__(singular_name, plural_name, abbreviations)
		
		self.n = n
		self.that = that
		
	def convert_to_internal(self, value, world=0.0):
		return self.that.convert_to_internal(value * self.n, world)
	
	def convert_from_internal(self, value, world=0.0):
		return self.that.convert_from_internal(value, world) / self.n