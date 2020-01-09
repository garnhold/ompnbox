import pdfex

import datetime


class IndirectObject_DocumentInformation(pdfex.IndirectObject_Dictionary):
	def __init__(self, title=None, author=None, subject=None, keywords=None, creator=None, producer=None):
		super(IndirectObject_DocumentInformation, self).__init__([
			pdfex.Entry_Value("title", "Title", title),
			pdfex.Entry_Value("author", "Author", author),
			pdfex.Entry_Value("subject", "Subject", subject),
			pdfex.Entry_Value("keywords", "Keywords", keywords),
			pdfex.Entry_Value("creator", "Creator", creator),
			pdfex.Entry_Value("producer", "Producer", producer),
			pdfex.Entry_Function("CreationDate", lambda: datetime.datetime.utcnow().strftime("D:%Y%m%d%H%M%SZ"))
		])