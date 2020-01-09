# import flect

import re


def is_identifier(value):
	if re.match("[A-Za-z_][A-Za-z0-9_]*", value):
		return True
	
	return False


def invariate_identifier(value):
	return re.sub('\s', "", value.lower())