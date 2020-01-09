#import pdfex

import oang
import types


class ValueRenderProvider_None(oang.ValueRenderProvider):
	def __init__(self):
		super(ValueRenderProvider_None, self).__init__(types.NoneType)
		
	def render(self, pdf_renderer, value):
		pdf_renderer.append_symbol("null")