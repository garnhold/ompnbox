import pdfex


class IndirectObject_Resources_Auto(pdfex.IndirectObject_Resources):
	def __init__(self, page):
		super(IndirectObject_Resources_Auto, self).__init__()
		
		self.page = page
		
	def get_xobjects(self):
		if self.page.contents:
			return self.page.contents.get_xobjects()
		
		return []