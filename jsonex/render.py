# import jsonex

import flect
import enumerable


def render_object(obj, renderer):
	renderer.append("{")
	renderer.start_section()
	
	enumerable.new(obj.__dict__.iteritems()) \
		.prepend_item(["@cls", type(obj).__name__]) \
		.process_interleaved(
			lambda p: render_pair(p[0], p[1], renderer),
			lambda: renderer.end_line(",")
		)
		
	renderer.end_section()
	renderer.append("}")


def render_dictionary(dictionary, renderer):
	if len(dictionary) <= 0:
		renderer.append("{}")
	else:
		renderer.append("{")
		renderer.start_section()
		
		enumerable.new(dictionary.iteritems()) \
			.process_interleaved(
				lambda p: render_pair(p[0], p[1], renderer),
				lambda: renderer.end_line(",")
			)
			
		renderer.end_section()
		renderer.append("}")


def render_list(lst, renderer):
	if len(lst) <= 0:
		renderer.append("[]")
	else:
		renderer.append("[")
		renderer.start_section()
		
		enumerable.new(lst) \
			.process_interleaved(
				lambda v: render_value(v, renderer),
				lambda: renderer.end_line(",")
			)
		
		renderer.end_section()
		renderer.append("]")


def render_pair(key, value, renderer):
	render_key(key, renderer)
	renderer.append(" : ")
	render_value(value, renderer)


def render_key(key, renderer):
	render_string(str(key), renderer)
	

def render_string(value, renderer):
	renderer.append(flect.encode_string_literal(value))


def render_bool(value, renderer):
	renderer.append(flect.encode_bool_literal(value).lower())
	

def render_value(value, renderer):
	if isinstance(value, dict):
		render_dictionary(value, renderer)
	elif isinstance(value, list):
		render_list(value, renderer)
	elif isinstance(value, basestring):
		render_string(value, renderer)
	elif isinstance(value, bool):
		render_bool(value, renderer)
	elif isinstance(value, (int, float)):
		renderer.append(str(value))
	elif hasattr(value, "__dict__"):
		render_object(value, renderer)
	else:
		render_string(str(value), renderer)