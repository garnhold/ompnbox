import pdfex


class Statement_PaintImage(pdfex.Statement):
	def __init__(self, xobject_image):
		super(Statement_PaintImage, self).__init__()
		
		self.xobject_image = xobject_image
	
	def render(self, content_renderer):
		content_renderer.append_line_format("{0} Do", self.xobject_image)
		
	def get_xobjects(self):
		return [self.xobject_image]