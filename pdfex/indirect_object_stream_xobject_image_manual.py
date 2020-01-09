import pdfex


class IndirectObject_Stream_XObject_Image_Manual(pdfex.IndirectObject_Stream_XObject_Image):
	def __init__(self, data, width, height, color_space=pdfex.Name("DeviceRGB"), bits_per_component=8, soft_mask=None, dpi=72.0, stream_filter_name="FlateDecode"):
		super(IndirectObject_Stream_XObject_Image_Manual, self).__init__(stream_filter_name)
		
		self.data = data
		self.width = width
		self.height = height
		self.color_space = color_space
		self.bits_per_component = bits_per_component
		self.soft_mask = soft_mask
		self.dpi = dpi
		
	def get_data(self):
		return self.data
		
	def get_width(self):
		return self.width
	
	def get_height(self):
		return self.height
	
	def get_color_space(self):
		return self.color_space
	
	def get_bits_per_component(self):
		return self.bits_per_component
	
	def get_soft_mask(self):
		return self.soft_mask
	
	def get_dpi(self):
		return self.dpi