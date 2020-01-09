import pdfex


class IndirectObject_Page(pdfex.IndirectObject_Dictionary):
	def __init__(self, contents=None, resources=None, bounds=None):
		super(IndirectObject_Page, self).__init__([
			pdfex.Entry_Constant("Type", pdfex.Name("Page")),
			pdfex.Entry_Constant("UserUnit", 72.0),
			pdfex.Entry_Value("parent", "Parent", None),
			pdfex.Entry_Value("resources", "Resources", resources),
			pdfex.Entry_Value("contents", "Contents", contents),
			pdfex.Entry_Value("bounds", "MediaBox", bounds)
		])