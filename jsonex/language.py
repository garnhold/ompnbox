# import jsonex

import lang
import collections


language = lang.LanguageEX()

OPEN_BRACE = language.make_literal_token("OPEN_BRACE", "{")
CLOSE_BRACE = language.make_literal_token("CLOSE_BRACE", "}")

OPEN_BRACKET = language.make_literal_token("OPEN_BRACKET", "[")
CLOSE_BRACKET = language.make_literal_token("CLOSE_BRACKET", "]")

COLON = language.make_literal_token("COLON", ":")
COMMA = language.make_literal_token("COMMA", ",")

STRING = language.make_pattern_token("STRING", "\"(\\\\\"|.)*?\"", lang.Interpreter_Token_QuotedString())
NUMBER = language.make_pattern_token("NUMBER", "[0-9\.\-]+", lang.Interpreter_Token_Float())
BOOL = language.make_literal_list_token("BOOL", ['true', 'false'], lang.Interpreter_Token_Bool())

WHITESPACE = language.make_pattern_token_ignore("WHITESPACE", "[ \t\n\r]+")


obj = language.create_phrase("obj")
lst = language.create_phrase("lst")

lstvalue = language.create_phrase("lstvalue")
attr = language.create_phrase("attr")

value = language.create_any("value")

value.initilize([
	NUMBER,
	STRING,
	BOOL,
	lst,
	obj
])

lstvalue.initilize([value], lang.Interpreter_CallMethod_Environment(list.append, [value]))
attr.initilize([STRING, COLON, value], lang.Interpreter_CallMethod_Environment(collections.OrderedDict.__setitem__, [STRING, value]))

lst.initilize([
	OPEN_BRACKET,
		language.create_interleaved("").initilize(lstvalue, COMMA),
	CLOSE_BRACKET
], lang.Interpreter_CallMethod_InstanceType(list))

obj.initilize([
	OPEN_BRACE,
		language.create_interleaved("").initilize(attr, COMMA),
	CLOSE_BRACE
], lang.Interpreter_CallMethod_InstanceType(collections.OrderedDict))