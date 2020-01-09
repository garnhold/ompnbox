#import timerex

import time


class Timer(object):
	def __init__(self, start=False):
		self.is_running = False
		self.start_time = 0.0
		self.stored_elapsed_time = 0.0
		
		if start:
			self.start()
			
	def start(self):
		if not self.is_running:
			self.start_time = time.time()
			self.is_running = True
			return True
			
		return False
		
	def stop(self):
		if self.is_running:
			self.stored_elapsed_time = self.get_elapsed_time()
			self.is_running = False
			return True
			
		return False
		
	def restart(self):
		self.clear()
		self.start()
		
	def clear(self):
		self.set_elapsed_time(0.0)
		
	def set_elapsed_time(self, elapsed_time):
		self.stored_elapsed_time = elapsed_time
		self.start_time = time.time()
	
	def get_lap_elapsed_time(self):
		if self.is_running:
			return time.time() - self.start_time
			
		return 0.0
		
	def get_stored_elapsed_time(self):
		return self.stored_elapsed_time
	
	def get_elapsed_time(self):
		return self.get_stored_elapsed_time() + self.get_lap_elapsed_time()
