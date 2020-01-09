#import bgon

import lang


language = lang.LanguageEX()

ADD = language.create_literal_token("ADD", "+")
SUBTRACT = language.create_literal_token("SUBTRACT", "-")
MULTIPLY = language.create_literal_token("MULTIPLY", "*")
DIVIDE = language.create_literal_token("DIVIDE", "/")

STRING = language.create_pattern_token("STRING", "\"(\\\\\"|.)*?\"", lang.Interpreter_Token_QuotedString())
NUMBER = language.create_pattern_token("NUMBER", "[0-9\.\-]+", lang.Interpreter_Token_Float())
BOOL = language.create_literal_list_token("BOOL", ['true', 'false'], lang.Interpreter_Token_Bool())
ID = language.create_pattern_token("ID", "[A-Za-z_][A-Za-z0-9_]*", lang.Interpreter_Token_String())

WHITESPACE = language.create_literal_list_token_ignore("WHITESPACE", ['\t', '\r', '\n', ' '])

EQUALS = language.create_literal_token("EQUALS", "=")

SEMI_COLON = language.create_literal_token("SEMI_COLON", ";")
PERIOD = language.create_literal_token("PERIOD", ".")
COMMA = language.create_literal_token("COMMA", ",")

OPEN_PAREN = language.create_literal_token("OPEN_PAREN", "(")
CLOSE_PAREN = language.create_literal_token("CLOSE_PAREN", ")")

OPEN_BRACKET = language.create_literal_token("OPEN_BRACKET", "[")
CLOSE_BRACKET = language.create_literal_token("CLOSE_BRACKET", "]")

OPEN_BRACE = language.create_literal_token("OPEN_BRACE", "{")
CLOSE_BRACE = language.create_literal_token("CLOSE_BRACE", "}")


obj = language.create_phrase("obj")

array = language.create_phrase("array")

identifier = language.create_phrase("identifier")

member = language.create_phrase("member")
member_assignment = language.create_phrase("member_assignment")

value_source = language.create_phrase("value_source")
value_destination = language.create_phrase("value_destination")


additive = language.create_any("additive").initilize([ADD, SUBTRACT])
multiplitive = language.create_any("multiplitive").initilize([MULTIPLY, DIVIDE])

expression = language.create_expression(value_source, [multiplitive, additive])


obj.initilize([
	ID,
	OPEN_PAREN,
		language.create_interleaved(value_source, COMMA),
	CLOSE_PAREN,
	OPEN_BRACE,
		language.create_repeating(member),
	CLOSE_BRACE
])

array.initilize([
	OPEN_BRACKET,
		language.create_interleaved(value_source, COMMA),
	CLOSE_BRACKET
])

identifier.initilize([
	language.create_any([
		ID
	])
])

member.initilize([
	language.create_any([
		member_assignment
	])
])

member_assignment.initilize([value_destination, EQUALS, value_source, SEMI_COLON])

value_source.initilize([
	language.create_any([
		identifier,
		array,
		
		NUMBER,
		BOOL,
		language.create_phrase("subexpression").initilize([OPEN_PAREN, value_source, CLOSE_PAREN])
	])
])

value_destination.initilize([
	language.create_any([
		ID
	])
])