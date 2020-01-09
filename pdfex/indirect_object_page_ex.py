import pdfex


class IndirectObject_PageEX(pdfex.IndirectObject_Page):
	def __init__(self, statements=None, bounds=None):
		super(IndirectObject_PageEX, self).__init__(
			pdfex.IndirectObject_Stream_Content(statements), 
			pdfex.IndirectObject_Resources_Auto(self),
			bounds
		)