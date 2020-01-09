#import helpers

import re


def get_expanded_dictionary_macro(dictionary, overrides):
	new_dictionary = {}
	
	for key, value in dictionary.iteritems():
		new_dictionary[key] = get_expanded_value_macro(value, overrides)
		
	return new_dictionary


def get_expanded_list_macro(lst, overrides):
	new_list = []
	
	for value in lst:
		new_list.append(get_expanded_value_macro(value, overrides))
		
	return new_list

			
def get_expanded_value_macro(value, overrides):
	if isinstance(value, basestring):
		match = re.search("^{([A-Za-z0-9_]+)}$", value)
			
		if match:
			label = match.group(1)
			if label in overrides:
				value = overrides[label]
				
		else:
			value = re.sub("{([A-Za-z0-9_]+)}", lambda m: overrides[m.group(1)], value)
			
	if isinstance(value, dict):
		value = get_expanded_dictionary_macro(value, overrides)
	elif isinstance(value, list):
		value = get_expanded_list_macro(value, overrides)
		
	return value


def get_list_macro_overrides(lst):
	overrides = []
	
	for value in lst:
		overrides.extend(get_value_macro_overrides(value))
		
	return overrides


def get_dictionary_macro_overrides(dictionary):
	overrides = []
	
	for key in dictionary:
		overrides.extend(get_value_macro_overrides(dictionary[key]))
		
	return overrides
	

def get_value_macro_overrides(value):
	overrides = []
	
	if isinstance(value, basestring):
		for override in re.findall('{([A-Za-z0-9_]+)}', value):
			overrides.append(override)
			
	elif isinstance(value, dict):
		overrides.extend(get_dictionary_macro_overrides(value))
	elif isinstance(value, list):
		overrides.extend(get_list_macro_overrides(value))
		
	return overrides


def get_unique_value_macro_overrides(value):
	return list(set(get_value_macro_overrides(value)))