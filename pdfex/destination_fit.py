import pdfex


class Destination_Fit(pdfex.Destination):
	def __init__(self, page):
		super(Destination_Fit, self).__init__(page, "Fit")