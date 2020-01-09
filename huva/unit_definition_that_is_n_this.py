import huva


class UnitDefinition_ThatIsNThis(huva.UnitDefinition_ThisIsNThat):
	def __init__(self, singular_name, plural_name, abbreviations, n, that):
		super(UnitDefinition_ThatIsNThis, self).__init__(singular_name, plural_name, abbreviations, 1.0 / n, that)