#import pdfex

import helpers
import flect


def fetch_stream_filter(name):
	return helpers.get_or_create_by_key(
		fetch_stream_filter.stream_filters,
		name,
		lambda k: flect.instance_subclass_by_suffix(StreamFilter, name)
	)
	
fetch_stream_filter.stream_filters = {}


class StreamFilter(object):
	def __init__(self):
		pass
	
	def encode_internal(self, data):
		return None
	
	def encode(self, data):
		if isinstance(data, list):
			data = "".join(data)
			
		return self.encode_internal(data)
	
	def get_name(self):
		return "None"