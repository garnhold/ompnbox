import pdfex

import oang


class ValueRenderProvider_NativePDFValue(oang.ValueRenderProvider):
	def __init__(self):
		super(ValueRenderProvider_NativePDFValue, self).__init__(pdfex.NativePDFValue)
		
	def render(self, pdf_renderer, value):
		value.render_pdf_value(pdf_renderer)