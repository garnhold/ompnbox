import pdfex

import mhat


class Statement_Transform(pdfex.Statement):
	def __init__(self, translation=None, rotation=None, scale=None):
		super(Statement_Transform, self).__init__()
		
		self.translation = translation
		self.rotation = rotation
		self.scale = scale
	
	def render(self, content_renderer):
		if self.translation:
			content_renderer.append_line_format(
				"1 0 0 1 {0} {1} cm",
				self.translation.get_x(),
				self.translation.get_y()
			)
		
		if self.rotation:
			rotation_sin = mhat.degrees.sin(self.rotation)
			rotation_cos = mhat.degrees.cos(self.rotation)
			content_renderer.append_line_format(
				"{0} {1} {2} {3} 0 0 cm",
				rotation_cos,
				rotation_sin,
				-rotation_sin,
				rotation_cos
			)
		
		if self.scale:
			content_renderer.append_line_format(
				"{0} 0 0 {1} 0 0 cm",
				self.scale.get_x(),
				self.scale.get_y()
			)
		
	def get_xobjects(self):
		return []