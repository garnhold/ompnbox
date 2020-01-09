#import cstr

import lect
import re
import rexex


class Escaper(object):
	def __init__(self, characters_to_escapes):
		self.characters_to_escapes = lect.BidirectionalDictionary(characters_to_escapes)
		
		self.regex_find_characters = re.compile(
			rexex.alternative_strings_group(self.characters_to_escapes.lefts())
		)
		
		self.regex_find_escapes = re.compile(
			rexex.alternative_strings_group(self.characters_to_escapes.rights())
		)
		
	def escape(self, value):
		return self.regex_find_characters.sub(
			lambda match: self.characters_to_escapes.get_right(match.group(1)),
			value
		)
		
	def unescape(self, value):
		return self.regex_find_escapes.sub(
			lambda match: self.characters_to_escapes.get_left(match.group(1)),
			value
		)
		