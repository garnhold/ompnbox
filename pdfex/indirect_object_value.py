import pdfex


class IndirectObject_Value(pdfex.IndirectObject):
	def __init__(self, value):
		super(IndirectObject_Value, self).__init__()
		
		self.value = value
		
	def render_object_internal(self, pdf_renderer):
		pdf_renderer.append_value(self.value)