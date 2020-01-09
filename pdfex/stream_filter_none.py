import pdfex


class StreamFilter_None(pdfex.StreamFilter):
	def __init__(self):
		super(StreamFilter_None, self).__init__()
		
	def encode_internal(self, data):
		return data
	
	def get_name(self):
		return None