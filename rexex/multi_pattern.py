#import rexex

import enumerable
import re


class MultiPattern(object):
	GROUP_PREFIX = "MULTI_"
	
	def __init__(self, patterns):
		self.patterns = patterns
		
		self.regex = re.compile(
			"(" + enumerable.new(self.patterns) \
					.convert_with_index(lambda p, i: "(?P<{0}>{1})".format(MultiPattern.GROUP_PREFIX + str(i), p)) \
					.str("|") + ")"
		)
		
		self.group_index_to_multi_index = enumerable.new(range(0, len(self.patterns))) \
			.dict_values(lambda i: self.regex.groupindex.get(MultiPattern.GROUP_PREFIX + str(i)))
			
	def match_all(self, text):
		for groups in self.regex.findall(text):
			index = enumerable.index(groups[1:], lambda s: s)
			multi_index = self.group_index_to_multi_index.get(index + 2)
			
			yield multi_index, groups[0]