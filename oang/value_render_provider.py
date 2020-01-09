#import oang

import flect


class ValueRenderProvider(flect.ClsHandlingProvider):
	def __init__(self, cls):
		super(ValueRenderProvider, self).__init__(cls)
		
	def render(self, renderer, value):
		pass