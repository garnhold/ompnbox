import huva


class UnitSystemEX(huva.UnitSystem):
	def __init__(self):
		super(UnitSystemEX, self).__init__()
		
	def add_internal(self, singular_name, plural_name, abbreviations):
		return self.add_unit_definition(huva.UnitDefinition_Internal(
			singular_name,
			plural_name,
			abbreviations
		))
		
	def add_ratio_of_world(self, singular_name, plural_name, abbreviations):
		return self.add_unit_definition(huva.UnitDefinition_RatioOfWorld(
			singular_name,
			plural_name,
			abbreviations
		))
		
	def add_this_is_n_that(self, singular_name, plural_name, abbreviations, n, that):
		return self.add_unit_definition(huva.UnitDefinition_ThisIsNThat(
			singular_name,
			plural_name,
			abbreviations,
			n,
			that
		))
			
	def add_that_is_n_this(self, singular_name, plural_name, abbreviations, n, that):
		return self.add_unit_definition(huva.UnitDefinition_ThatIsNThis(
			singular_name,
			plural_name,
			abbreviations,
			n,
			that
		))