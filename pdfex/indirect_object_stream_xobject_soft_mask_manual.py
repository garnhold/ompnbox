import pdfex


class IndirectObject_Stream_XObject_SoftMask_Manual(pdfex.IndirectObject_Stream_XObject_SoftMask):
	def __init__(self, data, width, height, bits_per_component=8, stream_filter_name="FlateDecode"):
		super(IndirectObject_Stream_XObject_SoftMask_Manual, self).__init__(stream_filter_name)
		
		self.data = data
		self.width = width
		self.height = height
		self.bits_per_component = bits_per_component
	
	def get_data(self):
		return self.data
		
	def get_width(self):
		return self.width
	
	def get_height(self):
		return self.height
	
	def get_bits_per_component(self):
		return self.bits_per_component