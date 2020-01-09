#import helpers

import re


def trim_whitespace(value):
	return re.sub("^\\s*(.+)\\s*$", "\\1", value)


def invariate(value):
	return re.sub('\\s', "", value.lower())


def trim_prefix(value, prefix):
	if value.startswith(prefix):
		return True, value[len(prefix):]
	
	return False, value


def trim_suffix(value, suffix):
	if value.endswith(suffix):
		return True, value[:-len(suffix)]
	
	return False, value


def prepend_prefix(value, prefix):
	if not value.startswith(prefix):
		return prefix + value
	
	return value


def append_suffix(value, suffix):
	if not value.endswith(suffix):
		return value + suffix
	
	return value