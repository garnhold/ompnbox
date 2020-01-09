#import cact


def default(value, default_value):
	if value is not None:
		return value
	
	return default_value


def defaults(values, default_values):
	to_return = []
	
	for i in range(0, len(values)):
		to_return.append(default(values[i], default_values[i]))
		
	return to_return


def default_list(value):
	if value is not None:
		return value
	
	return []


def default_dictionary(value):
	if value is not None:
		return value
	
	return {}