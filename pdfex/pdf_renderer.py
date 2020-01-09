import pdfex

import cact
import oang


class PDFRenderer(oang.RendererEX):
	def __init__(self):
		super(PDFRenderer, self).__init__([
			pdfex.ValueRenderProvider_Bool(),
			pdfex.ValueRenderProvider_Int(),
			pdfex.ValueRenderProvider_Float(),
			pdfex.ValueRenderProvider_String(),
			pdfex.ValueRenderProvider_Array(),
			pdfex.ValueRenderProvider_Dictionary(),
			pdfex.ValueRenderProvider_None(),
			
			pdfex.ValueRenderProvider_NativePDFValue(),
			
			pdfex.ValueRenderProvider_Rect2()
		], "\t", "\r\n")
		
		self.indirect_object_id_generator = cact.Generator_SequentialInt()
		
		self.indirect_objects = []
		self.unwritten_indirect_objects = []
		
	def append_symbol(self, symbol):
		self.append(symbol + " ")
		
	def append_value(self, value):
		if isinstance(value, pdfex.IndirectObject):
			self.append_indirect_object(value)
			
		oang.RendererEX.append_value(self, value)
		
	def append_pair(self, key, value):
		self.start_line()
		self.append_value(pdfex.Name(key))
		self.append_value(value)
		self.end_line()
				
	def append_indirect_object(self, obj):
		if obj is not None:
			if obj not in self.indirect_objects:
				obj.id = self.indirect_object_id_generator.generate()
				
				self.indirect_objects.append(obj)
				self.unwritten_indirect_objects.append(obj)
			
	def finalize(self, document_catalog, document_information):
		self.append_indirect_object(document_catalog)
		self.append_indirect_object(document_information)
		
		while len(self.unwritten_indirect_objects) > 0:
			self.unwritten_indirect_objects.pop().render_object(self)
			
		xref_offset = self.append_line_get_offset("xref")
		
		self.append_line("0 {0:d}".format(len(self.indirect_objects) + 1))
		
		self.append_line("0000000000 65535 f")
		for indirect_object in self.indirect_objects:
			indirect_object.render_xref_entry(self)
		
		self.append_line("trailer")
		self.start_section()
		self.append_value({
			"Size" : len(self.indirect_objects),
			"Info" : document_information,
			"Root" : document_catalog
		})
		self.end_section()
		
		self.append_line("startxref")
		self.append_line_value(xref_offset)
		
		self.start_line("%%EOF")