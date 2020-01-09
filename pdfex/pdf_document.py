import pdfex


class PDFDocument(object):
	def __init__(self):
		self.pages = pdfex.IndirectObject_PageTree()
		self.catalog = pdfex.IndirectObject_DocumentCatalog(self.pages)
		self.information = pdfex.IndirectObject_DocumentInformation()
		
	def render_pdf(self):
		return self.catalog.render_pdf(self.information)
		
	def render_pdf_to_file(self, filename):
		self.catalog.render_pdf_to_file(self.information, filename)