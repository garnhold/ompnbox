# import helpers

import flect


def parse_bool(value):
	if isinstance(value, basestring):
		return flect.decode_bool_literal(value)
	
	if value:
		return True
	
	return False