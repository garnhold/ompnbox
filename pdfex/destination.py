import pdfex


class Destination(pdfex.NativePDFValue):
	def __init__(self, page, destination_type):
		super(Destination, self).__init__()
		
		self.page = page
		self.destination_type = destination_type
		
	def render_pdf_value(self, pdf_renderer):
		pdf_renderer.append_value([
			self.page,
			pdfex.Name(self.destination_type)
		] + self.get_destination_arguments())
		
	def get_destination_arguments(self):
		return []