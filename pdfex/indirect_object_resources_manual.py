import pdfex

import cact


class IndirectObject_Resources_Manual(pdfex.IndirectObject_Resources):
	def __init__(self, xobjects):
		super(IndirectObject_Resources_Manual, self).__init__()
		
		self.xobjects = cact.default_list(xobjects)
		
	def get_xobjects(self):
		return self.xobjects