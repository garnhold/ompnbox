# import enumerable

import collections


def narrow(item, predicate):
	for sub_item in item:
		if predicate(sub_item):
			yield sub_item
			
			
def skip(item, predicate):
	for sub_item in item:
		if not predicate(sub_item):
			yield sub_item
			
			
def convert(item, operation):
	for sub_item in item:
		yield operation(sub_item)
		
		
def convert_with_index(item, operation):
	i = 0
	for sub_item in item:
		yield operation(sub_item, i)
		i += 1
		
		
def convert_identity(item, operation):
	converted_items = {}
	
	for sub_item in item:
		converted = converted_items.get(sub_item, None)
		if not converted:
			converted = operation(sub_item)
			converted_items[sub_item] = converted
			
		yield converted
		
		
def convert_as_keys(item, dictionary):
	for sub_item in item:
		yield dictionary[sub_item]


def chunk(item, limit, operation=lambda x: 1):
	amount = 0
	chunk = []

	for sub_item in item:
		amount += operation(sub_item)
		chunk.append(sub_item)

		if amount >= limit:
			yield chunk

			amount = 0
			chunk = []

	if chunk:
		yield chunk


def mchunk(item, *args):
	amounts = collections.defaultdict(int)
	chunk = []

	for sub_item in item:
		chunk.append(sub_item)

		for arg in args:
			amounts[arg] += arg[1](sub_item)

			if amounts[arg] >= arg[0]:
				yield chunk

				amounts = collections.defaultdict(int)
				chunk = []
				break

	if chunk:
		yield chunk


def end_before(item, predicate):
	for sub_item in item:
		if predicate(sub_item):
			return
		
		yield sub_item
		
		
def end_with(item, predicate):
	for sub_item in item:
		yield sub_item
		
		if predicate(sub_item):
			return


def seperate(item, predicate):
	true_items = []
	false_items = []
	
	for sub_item in item:
		if predicate(sub_item):
			true_items.append(sub_item)
		else:
			false_items.append(sub_item)
			
	return true_items, false_items


def sort_ascending(item, operation):
	return sorted(item, key=operation)


def sort_descending(item, operation):
	return sorted(item, key=lambda x: -operation(x))


def lst(item):
	return list(item)


def dct(item, operation):
	dictionary = {}
	
	for sub_item in item:
		key, value = operation(sub_item)
		dictionary[key] = value
		
	return dictionary


def dict_keys(item, operation):
	dictionary = {}
	
	for sub_item in item:
		dictionary[sub_item] = operation(sub_item)
		
	return dictionary
	
	
def dict_values(item, operation):
	dictionary = {}
	
	for sub_item in item:
		dictionary[operation(sub_item)] = sub_item
		
	return dictionary


def ordered_dict_keys(item, operation):
	dictionary = collections.OrderedDict()
	
	for sub_item in item:
		dictionary[sub_item] = operation(sub_item)
		
	return dictionary


def ordered_dict_values(item, operation):
	dictionary = collections.OrderedDict()
	
	for sub_item in item:
		dictionary[operation(sub_item)] = sub_item
		
	return dictionary


def merge(item):
	dictionary = {}
	
	for sub_item in item:
		dictionary.update(sub_item)
		
	return dictionary


def merge_ordered(item):
	dictionary = collections.OrderedDict()
	
	for sub_item in item:
		dictionary.update(sub_item)
		
	return dictionary


def flatten(item):
	for sub_item in item:
		for sub_sub_item in sub_item:
			yield sub_sub_item
			
			
def elongate(item):
	iterators = list(convert(item, lambda i: iter(i)))
	
	number_yielded = 1
	while number_yielded > 0:
		number_yielded = 0
		for iterator in iterators:
			try:
				yield next(iterator)
				number_yielded += 1
			except StopIteration:
				pass
			
def unique(item):
	working_set = set()
	
	for sub_item in item:
		if sub_item not in working_set:
			working_set.add(sub_item)
			yield sub_item
			
			
def append_item(item, to_append):
	for sub_item in item:
		yield sub_item
		
	yield to_append
	
	
def prepend_item(item, to_prepend):
	yield to_prepend
	
	for sub_item in item:
		yield sub_item
		
		
def append(item1, item2):
	for sub_item in item1:
		yield sub_item
		
	for sub_item in item2:
		yield sub_item
		
		
def prepend(item1, item2):
	for sub_item in item2:
		yield sub_item
		
	for sub_item in item1:
		yield sub_item
		
		
def interleave_item(item, seperator):
	iterator = iter(item)
	
	try:
		sub_item = next(iterator)
		
		while True:
			yield sub_item
	
			sub_item = next(iterator)
			yield seperator
	except StopIteration:
		pass


def index(item, predicate):
	i = 0
	for sub_item in item:
		if predicate(sub_item):
			return i
		
		i += 1


def find(item, predicate):
	for sub_item in item:
		if predicate(sub_item):
			return sub_item


def first(item):
	sub_item = None
	iterator = iter(item)
	
	try:
		sub_item = next(iterator)
	except StopIteration:
		return None
	
	return sub_item


def only(item):
	sub_item = None
	iterator = iter(item)
	
	try:
		sub_item = next(iterator)
		
		next(iterator)
	except StopIteration:
		return sub_item
	
	return None

		
def process(item, process):
	for sub_item in item:
		process(sub_item)
		
		
def process_interleaved(item, process, interleaved_process):
	iterator = iter(item)
	
	try:
		sub_item = next(iterator)
		
		while True:
			process(sub_item)
	
			sub_item = next(iterator)
			interleaved_process()
	except StopIteration:
		pass


def apply_to(item, value, operation):
	for sub_item in item:
		value = operation(value, sub_item)
	
	return value


def apply_to_first(item, operation):
	iterator = iter(item)
	
	try:
		value = next(iterator)
		
		while True:
			next_value = next(iterator)
			value = operation(value, next_value)
			
	except StopIteration:
		pass
	
	return value


def count(item, predicate):
	total = 0
	
	for sub_item in item:
		if predicate(sub_item):
			total += 1
			
	return total


def count_all(item):
	total = 0
	
	for _ in item:
		total += 1
		
	return total
		
		
def has(item, predicate):
	for sub_item in item:
		if predicate(sub_item):
			return True
		
	return False