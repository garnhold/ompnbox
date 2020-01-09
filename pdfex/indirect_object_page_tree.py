import pdfex


class IndirectObject_PageTree(pdfex.IndirectObject_Dictionary):
	def __init__(self, pages=None, parent=None):
		super(IndirectObject_PageTree, self).__init__([
			pdfex.Entry_Constant("Type", pdfex.Name("Pages")),
			pdfex.Entry_Value("pages", "Kids", []),
			pdfex.Entry_Value("parent", "Parent", parent),
			pdfex.Entry_Function("Count", lambda: len(self.pages))
		])
		
		if pages:
			self.add_pages(pages)
		
	def add_page(self, page):
		self.pages.append(page)
		page.parent = self
		
		return page
		
	def add_pages(self, pages):
		for page in pages:
			self.add_page(page)
			
	def __len__(self):
		return len(self.pages)
			
	def __iter__(self):
		return iter(self.pages)
	
	def __getitem__(self, index):
		return self.pages[index]