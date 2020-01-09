import algae

import cact


class System(object):
	def __init__(self, equations=None):
		self.equations = cact.default_list(equations)
		
	