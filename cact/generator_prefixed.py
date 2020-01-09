import cact


class Generator_Prefixed(cact.Generator):
	def __init__(self, prefix, internal_generator):
		self.prefix = prefix
		self.internal_generator = internal_generator 
		
	def generate(self):
		return self.prefix + str(self.internal_generator.generate())