#import pdfex

import oang
import enumerable


class ValueRenderProvider_Array(oang.ValueRenderProvider):
	def __init__(self):
		super(ValueRenderProvider_Array, self).__init__(list)
		
	def render(self, pdf_renderer, value):
		pdf_renderer.append("[")
		
		enumerable.new(value) \
			.process_interleaved(
				lambda v: pdf_renderer.append_value(v),
				lambda: pdf_renderer.append(" ")
			)
		
		pdf_renderer.append("]")