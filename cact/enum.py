#import cact

import enumerable
import flect


class EnumEntry(object):
	def __init__(self, name, identifier, enum=None):
		self.name = name
		self.identifier = identifier
		
		self.enum = enum
	
	def __repr__(self, *args, **kwargs):
		return "{0}.{1}({2})".format(self.enum, self.name, self.identifier)


class Enum(object):
	__SLOTS__ = [
		"name",
		"entrys",
		
		"entrys_by_name",
		"entrys_by_identifier"
	]
	
	def prepare_entrys(self, entrys):
		prepared = []
		
		if isinstance(entrys, dict):
			for key, value in entrys.iteritems():
				prepared.append(EnumEntry(key, value, self))
				
		elif isinstance(entrys, list):
			for value in entrys:
				if isinstance(value, EnumEntry):
					value.enum = self
					prepared.append(value)
				elif isinstance(value, basestring):
					prepared.append(EnumEntry(value, len(prepared), self))

		return prepared
	
	def __init__(self, name, entrys):
		self.name = name
		self.entrys = self.prepare_entrys(entrys)
		
		self.entrys_by_name = enumerable.new(self.entrys) \
			.dict_values(lambda e: flect.invariate_identifier(e.name))
			
		self.entrys_by_identifier = enumerable.new(self.entrys) \
			.dict_values(lambda e: e.identifier)
		
	def parse(self, value):
		if isinstance(value, EnumEntry):
			if value.enum == self:
				return value
		
		return self.get_by_name(value) or self.get_by_identifier(value)
		
	def get_by_name(self, name):
		return self.entrys_by_name.get(flect.invariate_identifier(name), None)
	
	def get_by_identifier(self, identifier):
		return self.entrys_by_identifier.get(identifier, None)
	
	def __getattr__(self, name):
		return self.get_by_name(name)
	
	def __iter__(self):
		return iter(self.entrys)
	
	def __repr__(self, *args, **kwargs):
		return self.name