#import spack


class PackedRect(object):
	__slots__ = [
		"size",
		"data",
		"rect",
		"is_flipped",
	]
	
	def __init__(self, size, data):
		self.size = size
		self.data = data
		
		self.rect = None
		self.is_flipped = False
		
	def pack(self, rect):
		self.rect = rect
		
		if self.rect.get_size().is_approximately_equal_to(self.size):
			self.is_flipped = False
		else:
			self.is_flipped = True
		
	def depack(self):
		self.rect = None
		self.is_flipped = False