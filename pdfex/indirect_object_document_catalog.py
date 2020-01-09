import pdfex

import filex


class IndirectObject_DocumentCatalog(pdfex.IndirectObject_Dictionary):
	def __init__(self, page_tree=None, open_action=None):
		super(IndirectObject_DocumentCatalog, self).__init__([
			pdfex.Entry_Constant("Type", pdfex.Name("Catalog")),
			pdfex.Entry_Value("page_tree", "Pages", page_tree),
			pdfex.Entry_Value("open_action", "OpenAction", open_action)
		])
		
	def render_pdf(self, document_information):
		renderer = pdfex.PDFRenderer()
		
		renderer.append_line("%PDF-1.6")
		renderer.finalize(self, document_information)
		return renderer.render()
		
	def render_pdf_to_file(self, document_information, filename):
		filex.fetch_file(filename).set_binary(self.render_pdf(document_information))