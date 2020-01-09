import pdfex


class IndirectObject(pdfex.NativePDFValue):
	def __init__(self):
		super(IndirectObject, self).__init__()
		
		self.id = None
		self.buffer_address = None
		
	def render_object_internal(self, pdf_renderer):
		pass
		
	def render_pdf_value(self, pdf_renderer):
		pdf_renderer.append_symbol("{0} 0 R".format(self.id))
		
	def render_object(self, pdf_renderer):
		self.buffer_address = pdf_renderer.append_line_get_offset("{0} 0 obj".format(self.id))
		pdf_renderer.start_section()
		
		self.render_object_internal(pdf_renderer)
		
		pdf_renderer.end_section()
		pdf_renderer.append_line("endobj")
		
	def render_xref_entry(self, pdf_renderer):
		pdf_renderer.append_line("{0:0>10d} {1:0>5d} n".format(self.buffer_address, 0))