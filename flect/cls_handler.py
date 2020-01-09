import flect

import helpers
import enumerable


class ClsHandler(object):
	def __init__(self, cls_handling_providers):
		self.cls_handling_providers = enumerable.new(cls_handling_providers) \
			.dict_values(lambda v: v.cls)
		
	def fetch_cls_handling_provider(self, cls):
		if cls:
			return helpers.get_or_create_by_key(
				self.cls_handling_providers, 
				cls,
				lambda t: enumerable.new(flect.get_all_base_classes(cls)) \
					.convert(lambda c: self.cls_handling_providers.get(c, None)) \
					.skip_none() \
					.first()
			)