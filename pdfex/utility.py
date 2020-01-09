import pdfex

import mhat
import enumerable
import spack


def create_image_pack_pdf(xobject_images, size):
	pdf = pdfex.PDFDocument()
	bounds = mhat.Rect2(size=size)
	
	to_pack = enumerable.new(xobject_images) \
		.convert(lambda i: spack.PackedRect(i.get_physical_size(), i)) \
		.lst()
	
	for sheet in spack.pack(bounds, to_pack):
		page = pdf.pages.add_page(pdfex.IndirectObject_PageEX(bounds=bounds))
		
		for rect in sheet:
			page.contents.statements.append(
				pdfex.Statement_Compound_PaintImage(rect.data, rect.rect.get_lower_left())
			)
			
	return pdf


def render_image_pack_pdf_to_file(xobject_images, size, filename):
	pdf = create_image_pack_pdf(xobject_images, size)
	pdf.catalog.open_action = pdfex.Destination_Fit(pdf.pages[0])
	
	pdf.render_pdf_to_file(filename)