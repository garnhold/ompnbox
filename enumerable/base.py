import enumerable


def new(enumerable):
	return Enumerable(enumerable)


class Enumerable(object):
	__slots__ = [
		"enumerable"
	]
	
	def __init__(self, enumerable):
		if enumerable is None:
			enumerable = []
			
		self.enumerable = enumerable
		
	def narrow(self, predicate):
		return Enumerable(enumerable.narrow(self.enumerable, predicate))
	
	def narrow_to_items(self, items):
		return self.narrow(lambda i: i in items)
	
	def skip(self, predicate):
		return Enumerable(enumerable.skip(self.enumerable, predicate))
	
	def skip_item(self, item):
		return self.skip(lambda i: i is item)
	
	def skip_items(self, items):
		return self.skip(lambda i: i in items)
	
	def skip_none(self):
		return self.skip(lambda i: i is None)
	
	def convert(self, operation):
		return Enumerable(enumerable.convert(self.enumerable, operation))
	
	def convert_with_index(self, operation):
		return Enumerable(enumerable.convert_with_index(self.enumerable, operation))
	
	def convert_identity(self, operation):
		return Enumerable(enumerable.convert_identity(self.enumerable, operation))
	
	def convert_as_keys(self, dictionary):
		return Enumerable(enumerable.convert_as_keys(self.enumerable, dictionary))

	def chunk(self, limit, operation=lambda x: 1):
		return Enumerable(enumerable.chunk(self.enumerable, limit, operation))

	def mchunk(self, *args):
		return Enumerable(enumerable.mchunk(self.enumerable, *args))

	def end_before(self, predicate):
		return Enumerable(enumerable.end_before(self.enumerable, predicate))
	
	def end_with(self, predicate):
		return Enumerable(enumerable.end_with(self.enumerable, predicate))
	
	def seperate(self, predicate):
		return enumerable.seperate(self.enumerable, predicate)
	
	def dict_keys(self, operation):
		return enumerable.dict_keys(self.enumerable, operation)
	
	def dict_values(self, operation):
		return enumerable.dict_values(self.enumerable, operation)
	
	def dct(self, operation):
		return enumerable.dct(self.enumerable, operation)
	
	def ordered_dict_keys(self, operation):
		return enumerable.ordered_dict_keys(self.enumerable, operation)
	
	def ordered_dict_values(self, operation):
		return enumerable.ordered_dict_values(self.enumerable, operation)
	
	def merge(self):
		return enumerable.merge(self.enumerable)
	
	def merge_ordered(self):
		return enumerable.merge_ordered(self.enumerable)
	
	def expand(self, operation):
		return self.convert(operation).flatten()
	
	def expandigate(self, operation):
		return self.convert(operation).elongate()
	
	def flatten(self):
		return Enumerable(enumerable.flatten(self.enumerable))
	
	def elongate(self):
		return Enumerable(enumerable.elongate(self.enumerable))
	
	def unique(self):
		return Enumerable(enumerable.unique(self.enumerable))
	
	def sort_ascending(self, operation):
		return Enumerable(enumerable.sort_ascending(self.enumerable, operation))
	
	def sort_descending(self, operation):
		return Enumerable(enumerable.sort_descending(self.enumerable, operation))
	
	def append(self, to_append):
		return Enumerable(enumerable.append(self.enumerable, to_append))
	
	def prepend(self, to_prepend):
		return Enumerable(enumerable.prepend(self.enumerable, to_prepend))
	
	def append_item(self, to_append):
		return Enumerable(enumerable.append_item(self.enumerable, to_append))
	
	def prepend_item(self, to_prepend):
		return Enumerable(enumerable.prepend_item(self.enumerable, to_prepend))
	
	def interleave_item(self, item):
		return Enumerable(enumerable.interleave_item(self.enumerable, item))
	
	def count(self, predicate):
		return enumerable.count(self.enumerable, predicate)
	
	def count_all(self):
		return enumerable.count_all(self.enumerable)
	
	def has(self, predicate):
		return enumerable.has(self.enumerable, predicate)
	
	def has_item(self, item):
		return self.has(lambda i: i == item)
	
	def process(self, process):
		enumerable.process(self.enumerable, process)
		
	def process_interleaved(self, process, interleaved_process):
		enumerable.process_interleaved(self.enumerable, process, interleaved_process)
	
	def index(self, predicate):
		return enumerable.index(self.enumerable, predicate)
	
	def find(self, predicate):
		return enumerable.find(self.enumerable, predicate)
	
	def first(self):
		return enumerable.first(self.enumerable)
	
	def only(self):
		return enumerable.only(self.enumerable)
	
	def apply(self, value, operation):
		return enumerable.apply_to(self.enumerable, value, operation)
	
	def apply_self(self, operation):
		return enumerable.apply_to_first(self.enumerable, operation)
	
	def sum(self):
		return sum(self.enumerable)
	
	def min(self):
		return min(self.enumerable)
	
	def max(self):
		return max(self.enumerable)
	
	def str(self, seperator=""):
		return seperator.join(self.convert(lambda i: str(i)))
	
	def lst(self):
		return enumerable.lst(self.enumerable)
	
	def set(self):
		return set(self.enumerable)
	
	def __iter__(self):
		return self.enumerable.__iter__()
	
	def __str__(self, *args, **kwargs):
		return self.str(", ")