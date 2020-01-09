import pdfex


class Name(pdfex.NativePDFValue, pdfex.NativeContentValue):
	def __init__(self, name):
		super(Name, self).__init__()
		
		self.name = name
		
	def render_pdf_value(self, pdf_renderer):
		pdf_renderer.append_symbol("/" + self.name)
		
	def render_content_value(self, content_renderer):
		content_renderer.append_symbol("/" + self.name)