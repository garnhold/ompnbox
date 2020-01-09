import pdfex

import mhat


class IndirectObject_Stream_XObject_Image(pdfex.IndirectObject_Stream_XObject):
	def __init__(self, stream_filter_name="FlateDecode"):
		super(IndirectObject_Stream_XObject_Image, self).__init__("Image", [
			pdfex.Entry_Function("Width", lambda: self.get_width()),
			pdfex.Entry_Function("Height", lambda: self.get_height()),
			pdfex.Entry_Function("ColorSpace", lambda: self.get_color_space()),
			pdfex.Entry_Function("BitsPerComponent", lambda: self.get_bits_per_component()),
			pdfex.Entry_Function("SMask", lambda: self.get_soft_mask())
		], stream_filter_name)
		
	def get_physical_width(self):
		return self.get_width() / self.get_dpi()
	
	def get_physical_height(self):
		return self.get_height() / self.get_dpi()
	
	def get_physical_size(self):
		return mhat.Vector2(self.get_physical_width(), self.get_physical_height())
		
	def get_width(self):
		return 0
	
	def get_height(self):
		return 0
	
	def get_size(self):
		return mhat.Vector2(self.get_width(), self.get_height())
	
	def get_color_space(self):
		return None
	
	def get_bits_per_component(self):
		return 0
	
	def get_soft_mask(self):
		return None
	
	def get_dpi(self):
		return 1.0