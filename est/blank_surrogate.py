# import est


class BlankSurrogate(object):
	def __getattr__(self, attr):
		return BlankSurrogate()
	
	def __call__(self, *args, **kwargs):
		return BlankSurrogate()