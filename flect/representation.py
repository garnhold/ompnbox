#import flect

import enumerable


def repr_string(obj, string):
	return "<{0}.{1}: {2}>".format(type(obj).__module__, type(obj).__name__, string)


def repr_self(obj):
	return repr_string(obj, str(obj))


def repr_self_and_values(obj, values):
	return repr_string(obj, str(obj) + " : " + enumerable.new(values).str(", "))


def repr_values(obj, values):
	return repr_string(obj, enumerable.new(values).str(", "))