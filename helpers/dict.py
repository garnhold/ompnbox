import helpers


def get_or_create_by_key(dictionary, key, operation):
	if key in dictionary:
		return dictionary[key]

	value = operation(key)
	dictionary[key] = value
	return value
	

def get_merged_overwrite_dictionarys(dictionary1, dictionary2):
	merged = dictionary1.copy()
	
	for key in dictionary2:
		merged[key] = dictionary2[key]
		
	return merged


def get_merged_combined_dictionarys(dictionary1, dictionary2):
	merged = dictionary1.copy()
	
	for key in dictionary2:
		merged[key] = helpers.get_combined(merged[key], dictionary2[key])
		
	return merged