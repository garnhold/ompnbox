# import flect

import cstr


STRING_ESCAPER = cstr.Escaper({
	'\\' : '\\\\',
	
	'"' : '\\"',
	
	'\n' : '\\n',
	'\r' : '\\r',
	'\t' : '\\t'
})


def encode_string_literal(text):
	return '"' + STRING_ESCAPER.escape(text) + '"'


def decode_string_literal(text):
	if text.startswith('"') and text.endswith('"'):
		return STRING_ESCAPER.unescape(text[1:-1])
	
	return None