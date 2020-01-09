import pdfex

import enumerable


class IndirectObject_Dictionary(pdfex.IndirectObject):
	def __init__(self, entrys):
		super(IndirectObject_Dictionary, self).__init__()
		
		self.entrys = []
		self.entry_values = {}
		
		for entry in entrys:
			self.entrys.append(entry)
			
			if isinstance(entry, pdfex.Entry_Value):
				self.entry_values[entry.variable_name] = entry
		
	def render_object_internal(self, pdf_renderer):
		pdf_renderer.append_value(self.get_entrys())
		
	def get_entrys(self):
		return enumerable.new(self.entrys) \
			.dct(lambda e: [e.name, e.get_value()])
			
	def __setattr__(self, name, value):
		if "entry_values" in self.__dict__ and name in self.entry_values:
			self.entry_values[name].set_value(value)
		else:
			super(IndirectObject_Dictionary, self).__setattr__(name, value)
			
	def __getattr__(self, name):
		if "entry_values" in self.__dict__ and name in self.entry_values:
			return self.entry_values[name].get_value()