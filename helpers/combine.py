#import helpers


def get_combined(value1, value2):
	if value1 is None:
		return value2
	
	if value2 is None:
		return value1
	
	if isinstance(value1, list):
		return value1 + value2
	
	if isinstance(value2, list):
		return value2 + value1
		
	return [value1, value2]
			