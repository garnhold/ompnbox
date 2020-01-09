#import oang

import flect


class ValueRenderer(flect.ClsHandler):
	def __init__(self, value_render_providers):
		super(ValueRenderer, self).__init__(value_render_providers)
		
	def render(self, renderer, value):
		cls = type(value)
		
		cls_handling_provider = self.fetch_cls_handling_provider(cls) 
		if cls_handling_provider:
			cls_handling_provider.render(renderer, value)
		else:
			raise ValueError("A ValueRenderProvider isn't registered for {0}".format(cls))