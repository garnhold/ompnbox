# import flect

import enumerable


def get_base_class(cls):
	return cls.__base__


def get_all_base_classes(cls):
	return enumerable.new(cls.__bases__) \
		.expandigate(lambda x: get_all_base_classes_with_self(x))
		

def get_all_base_classes_with_self(cls):
	return enumerable.new(get_all_base_classes(cls)) \
		.prepend_item(cls)


def get_all_subclasses(cls):
	return enumerable.new(cls.__subclasses__()) \
		.expand(lambda x: get_all_subclasses_with_self(x))
		
		
def get_all_subclasses_with_self(cls):
	return enumerable.new(get_all_subclasses(cls)) \
		.prepend_item(cls)


def get_subclass_by_name(cls, name):
	return get_all_subclasses(cls).find(lambda x: x.__name__ == name)


def instance_subclass_by_name(cls, name, *args, **kwargs):
	subclass = get_subclass_by_name(cls, name)
	
	if subclass:
		return subclass(*args, **kwargs)
	

def instance_subclass_by_suffix(cls, suffix, *args, **kwargs):
	return instance_subclass_by_name(cls, cls.__name__ + "_" + suffix, *args, **kwargs)