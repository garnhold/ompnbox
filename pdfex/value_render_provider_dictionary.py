#import pdfex

import oang
import enumerable


class ValueRenderProvider_Dictionary(oang.ValueRenderProvider):
	def __init__(self):
		super(ValueRenderProvider_Dictionary, self).__init__(dict)
		
	def render(self, pdf_renderer, value):
		if len(value) <= 0:
			pdf_renderer.append("<< >>")
		else:
			pdf_renderer.append("<<")
			pdf_renderer.start_section()
			
			enumerable.new(value.iteritems()) \
				.skip(lambda p: p[1] is None) \
				.process(
					lambda p: pdf_renderer.append_pair(p[0], p[1])
				)
			
			pdf_renderer.end_section()
			pdf_renderer.append(">>")