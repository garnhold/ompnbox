import pdfex


class Destination_Manual(pdfex.Destination):
	def __init__(self, page, x=None, y=None, zoom=None):
		super(Destination_Manual, self).__init__(page, "XYZ")
		
		self.x = x
		self.y = y
		self.zoom = zoom
		
	def get_destination_arguments(self):
		return [self.x, self.y, self.zoom]