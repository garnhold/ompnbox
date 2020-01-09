import oang


class Indentation_Suspendable(oang.Indentation):
	def __init__(self, indent="\t"):
		super(Indentation_Suspendable, self).__init__(indent)
		
		self.suspension_level = 0
		
	def suspend(self):
		self.suspension_level += 1
		
	def resume(self):
		self.suspension_level -= 1
		
	def is_suspended(self):
		if self.suspension_level > 0:
			return True
		
		return False
		
	def get_indentation_string(self):
		if self.is_suspended():
			return ""
		
		return oang.Indentation.get_indentation_string(self)
	
	def get_indentation_length(self):
		if self.is_suspended():
			return 0
		
		return oang.Indentation.get_indentation_length(self)