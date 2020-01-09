import mhat


class Vector2Base(object):
	def __init__(self):
		pass
	
	def get_x(self):
		return None
	
	def get_y(self):
		return None
	
	def get_min(self):
		return min(self.get_x(), self.get_y())
	
	def get_max(self):
		return max(self.get_x(), self.get_y())
		
	def get_with_x(self, x):
		return mhat.Vector2(x, self.get_y())
	
	def get_with_y(self, y):
		return mhat.Vector2(self.get_x(), y)
	
	def get_with_adjusted_x(self, x):
		return self.get_with_x(self.get_x() + x)
	
	def get_with_adjusted_y(self, y):
		return self.get_with_y(self.get_y() + y)
	
	def get_swapped(self):
		return mhat.Vector2(self.get_y(), self.get_x())
	
	def dot(self, other):
		return self.get_x() * other.get_x() + self.get_y() + other.get_y()
	
	def order(self, other):
		min_x, max_x = mhat.order(self.get_x(), other.get_x())
		min_y, max_y = mhat.order(self.get_y(), other.get_y())
		
		return mhat.Vector2(min_x, min_y), mhat.Vector2(max_x, max_y)
	
	def is_approximately_equal_to(self, other, percision=1e-10):
		x = abs(self.get_x() - other.get_x())
		if x > percision:
			return False
		
		y = abs(self.get_y() - other.get_y())
		if y > percision:
			return False
		
		return True
		
	def __add__(self, other):
		return mhat.Vector2(self.get_x() + other.get_x(), self.get_y() + other.get_y())
	
	def __sub__(self, other):
		return mhat.Vector2(self.get_x() - other.get_x(), self.get_y() - other.get_y())
	
	def __mul__(self, scalar):
		if isinstance(scalar, (int, float, long)):
			return mhat.Vector2(self.get_x() * scalar, self.get_y() * scalar)
		
		return NotImplemented
	__rmul__ = __mul__
	
	def __div__(self, scalar):
		if isinstance(scalar, (int, float, long)):
			return mhat.Vector2(self.get_x() / scalar, self.get_y() / scalar)
		
		return NotImplemented
	
	def __str__(self, *args, **kwargs):
		return "<{0}, {1}>".format(self.get_x(), self.get_y())
	
	def __repr__(self, *args, **kwargs):
		return "Vector2({0}, {1})".format(self.get_x(), self.get_y())