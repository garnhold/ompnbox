#import rexex

import enumerable
import re


def alternative_strings(strings):
	return enumerable.new(strings) \
		.convert(lambda s: re.escape(s)) \
		.str("|")
		

def alternative_strings_group(strings):
	return "(" + alternative_strings(strings) + ")"