import pdfex


class IndirectObject_Stream_XObject_SoftMask(pdfex.IndirectObject_Stream_XObject):
	def __init__(self, stream_filter_name="FlateDecode"):
		super(IndirectObject_Stream_XObject_SoftMask, self).__init__("Image", [
			pdfex.Entry_Function("Width", lambda: self.get_width()),
			pdfex.Entry_Function("Height", lambda: self.get_height()),
			pdfex.Entry_Constant("ColorSpace", pdfex.Name("DeviceGray")),
			pdfex.Entry_Function("BitsPerComponent", lambda: self.get_bits_per_component())
		], stream_filter_name)
		
	def get_width(self):
		return 0
	
	def get_height(self):
		return 0
	
	def get_bits_per_component(self):
		return 0