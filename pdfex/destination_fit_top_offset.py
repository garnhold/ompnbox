import pdfex


class Destination_FitTopOffset(pdfex.Destination):
	def __init__(self, page, offset):
		super(Destination_FitTopOffset, self).__init__(page, "FitH")
		
		self.offset = offset
		
	def get_destination_arguments(self):
		return [self.offset]