import pdfex

import enumerable


class IndirectObject_Resources(pdfex.IndirectObject_Dictionary):
	def __init__(self):
		super(IndirectObject_Resources, self).__init__([
			pdfex.Entry_Constant("ProcSet", [
				pdfex.Name("PDF"),
				pdfex.Name("Text"),
				pdfex.Name("ImageB"),
				pdfex.Name("ImageC"),
				pdfex.Name("ImageI")
			]),
			pdfex.Entry_Function("XObject", lambda: self.get_xobject_entrys())
		])
		
	def get_xobjects(self):
		return []
		
	def get_xobject_entrys(self):
		return enumerable.new(self.get_xobjects()) \
			.dct(lambda x: [x.name, x])