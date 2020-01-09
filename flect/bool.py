import flect

BOOL_VALUE_TABLE = {
	"true" : True,
	"yes" : True,
	"1" : True,
	"t" : True,
	"y" : True,
	"on" : True,
	"confirm" : True,
	"accept" : True,
	
	"false" : False,
	"no" : False,
	"0" : False,
	"f" : False,
	"n" : False,
	"off" : False,
	"dismiss" : False,
	"deny" : False
}

def encode_bool_literal(value):
	if value:
		return "True"
	
	return "False"


def decode_bool_literal(value):
	return BOOL_VALUE_TABLE.get(flect.invariate_identifier(value), False)