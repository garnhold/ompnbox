#import pdfex

import oang


class ValueRenderProvider_Int(oang.ValueRenderProvider):
	def __init__(self):
		super(ValueRenderProvider_Int, self).__init__(int)
		
	def render(self, pdf_renderer, value):
		pdf_renderer.append_symbol("{0:d}".format(value))