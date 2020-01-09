import log


def announce(start, check=False):
	def decorator(func):
		def wrap(*args, **kwargs):
			log.message(start)
			log.indent()

			return_value = None

			try:
				return_value = func(*args, **kwargs)
			except:
				log.exception()

			if check:
				if not return_value:
					log.error("Failure")

			log.dedent()

			return return_value
		return wrap
	return decorator