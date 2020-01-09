#import huva

import enumerable
import flect


class UnitDefinition(object):
	def __init__(self, singular_name, plural_name, abbreviations):
		self.singular_name = singular_name
		self.plural_name = plural_name
		
		self.abbreviations = abbreviations
		
		self.identifiers = enumerable.new(self.abbreviations) \
			.append_item(self.singular_name) \
			.append_item(self.plural_name) \
			.convert(lambda s: flect.invariate_identifier(s)) \
			.set() 
		
	def convert_to_internal(self, value, world=0.0):
		return 0.0
	
	def convert_from_internal(self, value, world=0.0):
		return 0.0
	
	def check_identifier(self, identifier):
		if flect.invariate_identifier(identifier) in self.identifiers:
			return True
		
		return False