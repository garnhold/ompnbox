import pdfex

import cact


class IndirectObject_Stream(pdfex.IndirectObject_Dictionary):
	def __init__(self, additional_entrys=None, stream_filter_name="FlateDecode"):
		super(IndirectObject_Stream, self).__init__([
			pdfex.Entry_Function("Filter", lambda: self.stream_filter.get_name()),
			pdfex.Entry_Function("Length", lambda: len(self.get_encoded_data()))
		] + cact.default_list(additional_entrys))
		
		self.stream_filter = pdfex.fetch_stream_filter(stream_filter_name)
		
	def render_object_internal(self, pdf_renderer):
		pdfex.IndirectObject_Dictionary.render_object_internal(self, pdf_renderer)
		
		pdf_renderer.suspend_indentation()
		
		pdf_renderer.append_line("stream")
		pdf_renderer.append(self.get_encoded_data())
		pdf_renderer.append_line("endstream")
		
		pdf_renderer.resume_indentation()
		
	def get_data(self):
		return ""
		
	def get_encoded_data(self):
		return self.stream_filter.encode(self.get_data())