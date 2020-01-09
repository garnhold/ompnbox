#import mhat


def order(a, b):
	if a < b:
		return a, b
		
	return b, a


def bind_above(value, a):
	if value < a:
		return a
		
	return value
	
	
def bind_below(value, b):
	if value > b:
		return b
		
	return value
	
	
def bind_between(value, a, b):
	a, b = order(a, b)
	
	if value < a:
		return a
		
	if value > b:
		return b
		
	return value
