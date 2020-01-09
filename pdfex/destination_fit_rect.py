import pdfex


class Destination_FitRect(pdfex.Destination):
	def __init__(self, page, rect):
		super(Destination_FitRect, self).__init__(page, "FitR")
		
		self.rect = rect
		
	def get_destination_arguments(self):
		return [
			self.rect.get_left(),
			self.rect.get_lower(),
			self.rect.get_right(),
			self.rect.get_upper()
		]