import pdfex

import zlib


class StreamFilter_FlateDecode(pdfex.StreamFilter):
	def __init__(self, level=6):
		super(StreamFilter_FlateDecode, self).__init__()
		
		self.level = level
		
	def encode_internal(self, data):
		return zlib.compress(data, self.level)
	
	def get_name(self):
		return pdfex.Name("FlateDecode")