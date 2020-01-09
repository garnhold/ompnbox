#import pdfex

import oang
import cstr


STRING_ESCAPER = cstr.Escaper({
	'\\' : '\\\\',
	
	'(' : '\\(',
	')' : '\\)',
	
	'\n' : '\\n',
	'\r' : '\\r',
	'\t' : '\\t'
})


class ValueRenderProvider_String(oang.ValueRenderProvider):
	def __init__(self):
		super(ValueRenderProvider_String, self).__init__(basestring)
		
	def render(self, pdf_renderer, value):
		pdf_renderer.append_symbol("(" + STRING_ESCAPER.escape(value) + ")")