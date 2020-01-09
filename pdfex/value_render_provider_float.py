#import pdfex

import oang
import flect


class ValueRenderProvider_Float(oang.ValueRenderProvider):
	def __init__(self):
		super(ValueRenderProvider_Float, self).__init__(float)
		
	def render(self, pdf_renderer, value):
		pdf_renderer.append_symbol(flect.encode_float_literal(value, 5))