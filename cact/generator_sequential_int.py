import cact


class Generator_SequentialInt(cact.Generator):
	def __init__(self, first_int_id=1):
		self.next_int_id = first_int_id
		
	def generate(self):
		int_id = self.next_int_id
		
		self.next_int_id += 1
		return int_id