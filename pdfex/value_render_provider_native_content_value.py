import pdfex

import oang


class ValueRenderProvider_NativeContentValue(oang.ValueRenderProvider):
	def __init__(self):
		super(ValueRenderProvider_NativeContentValue, self).__init__(pdfex.NativeContentValue)
		
	def render(self, content_renderer, value):
		value.render_content_value(content_renderer)