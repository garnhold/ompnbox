import pdfex

import cact


XOBJECT_NAME_GENERATOR = cact.Generator_Prefixed("Obj", cact.Generator_SequentialInt())


class IndirectObject_Stream_XObject(pdfex.IndirectObject_Stream, pdfex.NativeContentValue):
	def __init__(self, sub_type, additional_entrys=None, stream_filter_name="FlateDecode"):
		super(IndirectObject_Stream_XObject, self).__init__([
			pdfex.Entry_Constant("Type", pdfex.Name("XObject")),
			pdfex.Entry_Constant("Subtype", pdfex.Name(sub_type))
		] + cact.default_list(additional_entrys), stream_filter_name)
		
		self.name = XOBJECT_NAME_GENERATOR.generate()
		
	def render_content_value(self, content_renderer):
		content_renderer.append_value(pdfex.Name(self.name))