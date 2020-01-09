#import pdfex

import oang


class ValueRenderProvider_Bool(oang.ValueRenderProvider):
	def __init__(self):
		super(ValueRenderProvider_Bool, self).__init__(bool)
		
	def render(self, pdf_renderer, value):
		if value:
			pdf_renderer.append_symbol("true")
		else:
			pdf_renderer.append_symbol("false")