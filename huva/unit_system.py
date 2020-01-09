import huva

import re


class UnitSystem(object):
	def __init__(self):
		self.unit_definitions = []
	
	def add_unit_definition(self, unit_definition):
		self.unit_definitions.append(unit_definition)
		return unit_definition
	
	def parse(self, value, world=0.0):
		if isinstance(value, (int, float, long)):
			return value
		
		if isinstance(value, basestring):
			match = re.match("^\\s*([0-9\\.\\-]+)\\s*(\\S*)\\s*$", value)
			
			if match:
				number = float(match.group(1))
				unit_definition = self.parse_unit_definition(match.group(2))
				
				if unit_definition:
					return unit_definition.convert_to_internal(number, world)
				
				return number
			
			return float(value)
				
		return 0.0
	
	def parse_to(self, value, dst_units, world=0.0):
		return self.parse_unit_definition(dst_units).convert_from_internal(
			self.parse(value, world), world
		)
		
	def convert(self, value, src_units, dst_units, world=0.0):
		src_units = self.parse_unit_definition(src_units)
		dst_units = self.parse_unit_definition(dst_units)
		
		return dst_units.convert_from_internal(src_units.convert_to_internal(value, world), world)
	
	def parse_unit_definition(self, identifier):
		if isinstance(identifier, huva.UnitDefinition):
			return identifier
		
		if isinstance(identifier, basestring):
			for unit_definition in self.unit_definitions:
				if unit_definition.check_identifier(identifier):
					return unit_definition
			
		return None