import prof


def profile_method(logger=None):
	def decorator(func):
		method_info = prof.MethodInfo(func)
		
		def wrap(*args, **kwargs):
			try:
				return method_info.invoke(*args, **kwargs)
			finally:
				if logger:
					logger.log_message(prof.render())
		
		return wrap
	return decorator