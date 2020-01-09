import prof


class MethodInfo(object):
	def __init__(self, method):
		self.method = method
		
		self.method_instances = []
		
	def invoke(self, *args, **kwargs):
		return prof.METHOD_INSTANCE_STACK[-1].invoke_child(self, *args, **kwargs)
	
	def __str__(self, *args, **kwargs):
		return "{0}::{1}".format(self.method.__module__, self.method.__name__)