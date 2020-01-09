#import flect


def encode_float_literal(value, max_digits_past_zero=32):
	full = "{0:.32f}".format(value)
	whole, fractional = full.split(".")
	
	if len(whole) <= 0:
		whole = "0"
	
	fractional = fractional[:max_digits_past_zero]
	fractional = fractional.rstrip("0")
	if len(fractional) <= 0:
		fractional = "0"
		
	return whole + "." + fractional