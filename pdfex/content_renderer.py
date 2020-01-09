import pdfex

import oang


class ContentRenderer(oang.RendererEX):
	def __init__(self):
		super(ContentRenderer, self).__init__([
			pdfex.ValueRenderProvider_Bool(),
			pdfex.ValueRenderProvider_Int(),
			pdfex.ValueRenderProvider_Float(),
			pdfex.ValueRenderProvider_String(),
			pdfex.ValueRenderProvider_NativeContentValue(),
			
			pdfex.ValueRenderProvider_Rect2()
		], "\t", "\r\n")
		
	def append_symbol(self, symbol):
		self.append(symbol + " ")