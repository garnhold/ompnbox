import pdfex


class Destination_FitLeftOffset(pdfex.Destination):
	def __init__(self, page, offset):
		super(Destination_FitLeftOffset, self).__init__(page, "FitV")
		
		self.offset = offset
		
	def get_destination_arguments(self):
		return [self.offset]