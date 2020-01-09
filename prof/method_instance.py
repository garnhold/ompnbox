import prof

import timerex
import helpers
import enumerable
import oang


class MethodInstance(object):
	def __init__(self, method_info, method_instance):
		self.method_info = method_info
		if self.method_info:
			self.method_info.method_instances.append(self)
		
		self.timer = timerex.Timer()
		self.child_method_instances = {}
		self.parent_method_instance = method_instance
		
	def invoke_child(self, method_info, *args, **kwargs):
		return helpers.get_or_create_by_key(
			self.child_method_instances,
			method_info, 
			lambda k: MethodInstance(method_info, self)
		).invoke(*args, **kwargs)
			
	def invoke(self, *args, **kwargs):
		try:
			prof.METHOD_INSTANCE_STACK.append(self)
			
			self.timer.start()
			return self.method_info.method(*args, **kwargs)
		finally:
			self.timer.stop()
			
			prof.METHOD_INSTANCE_STACK.pop()
			
	def get_total_time(self):
		return self.timer.get_elapsed_time()
	
	def get_child_time(self):
		return enumerable.new(self.child_method_instances.values()) \
			.convert(lambda c: c.get_total_time()) \
			.sum()
			
	def get_parent_time(self):
		if self.parent_method_instance:
			return self.parent_method_instance.get_total_time()
		
		return 0.0
	
	def get_self_time(self):
		return self.get_total_time() - self.get_child_time()
			
	def get_percent_of_parent(self):
		parent_time = self.get_parent_time()
		
		if parent_time:
			return self.get_total_time() / parent_time
		
		return 1.0
	
	def get_percent_of_total(self):
		total_time = self.get_total_time()
		
		if total_time:
			return self.get_self_time() / total_time
		
		return 1.0
	
	def render(self):
		renderer = oang.Renderer()
		
		self.render_to(renderer)
		return renderer.render()
	
	def render_to(self, renderer):
		renderer.start_line()
		renderer.append(str(self.method_info))
		renderer.append("({0:.3f}s, {1:.2f}% of parent)  ".format(self.get_total_time(), self.get_percent_of_parent() * 100.0))
		renderer.append("({0:.3f}s, {1:.2f}% of self)  ".format(self.get_self_time(), self.get_percent_of_total() * 100.0))
		
		if len(self.child_method_instances):
			renderer.append_line("{")
			renderer.start_section()
			
			enumerable.new(self.child_method_instances.values()) \
				.process(
					lambda v: v.render_to(renderer)
				)
			
			renderer.end_section()
			renderer.append_line("}")
			
		renderer.end_line()