#import pdfex

import oang
import mhat


class ValueRenderProvider_Rect2(oang.ValueRenderProvider):
	def __init__(self):
		super(ValueRenderProvider_Rect2, self).__init__(mhat.Rect2)
		
	def render(self, pdf_renderer, value):
		pdf_renderer.append_value([
			value.get_left(), value.get_lower(), value.get_right(), value.get_upper()
		])