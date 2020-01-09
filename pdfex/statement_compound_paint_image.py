import pdfex

import mhat


class Statement_Compound_PaintImage(pdfex.Statement_Compound):
	def __init__(self, xobject_image, position=None, rotation=None, scale=None):
		if not scale:
			scale = mhat.Fector2(
				lambda: self.paint_image.xobject_image.get_physical_width(),
				lambda: self.paint_image.xobject_image.get_physical_height()
			)
		
		self.paint_image = pdfex.Statement_PaintImage(xobject_image)
		self.transform = pdfex.Statement_Transform(position, rotation, scale)
		
		self.graphics_state_block = pdfex.Statement_GraphicsStateBlock([
			self.transform,
			self.paint_image
		])
		
		super(Statement_Compound_PaintImage, self).__init__([
			self.graphics_state_block
		])