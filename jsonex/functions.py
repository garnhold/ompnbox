import jsonex

import oang
import prof


@prof.profile_method()
def serialize(obj):
	renderer = oang.Renderer()
	
	jsonex.render_value(obj, renderer)
	return renderer.render()


@prof.profile_method()
def deserialize(string):
	return jsonex.value.parse_text(string)