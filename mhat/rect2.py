import mhat


def create_min_max_rect2(point1, point2):
	lower, upper = point1.order(point2)
	
	return Rect2(lower, upper - lower)


class Rect2(object):
	__slots__ = [
		"_position",
		"_size"
	]
	
	def __init__(self, position=mhat.Vector2(), size=mhat.Vector2()):
		self._position = position
		self._size = size
		
	def quadsect(self, position):
		if self.is_point_within(position):
			return [
				create_min_max_rect2(self.get_lower_left(), position),
				create_min_max_rect2(self.get_lower_right(), position),
				create_min_max_rect2(self.get_upper_right(), position),
				create_min_max_rect2(self.get_upper_left(), position)
			]
			
		return None
	
	def quadsect_lower_left_offset(self, offset):
		return self.quadsect(self.get_lower_left() + offset)
		
	def get_with_position(self, position):
		return Rect2(position, self._size)
	
	def get_with_size(self, size):
		return Rect2(self._position, size)
	
	def get_with_adjusted_position(self, position):
		return self.get_with_position(self._position + position)
	
	def get_with_adjusted_size(self, size):
		return self.get_with_size(self._size + size)
		
	def is_point_within(self, point):
		if point.get_x() >= self.get_left() and point.get_x() <= self.get_right():
			if point.get_y() >= self.get_lower() and point.get_y() <= self.get_upper():
				return True
			
		return False
	
	def get_left(self):
		return self._position.get_x()
	
	def get_right(self):
		return self._position.get_x() + self.get_width()
	
	def get_lower(self):
		return self._position.get_y()
	
	def get_upper(self):
		return self._position.get_y() + self.get_height()
		
	def get_center(self):
		return self._position + self._size * 0.5
		
	def get_lower_left(self):
		return mhat.Vector2(self.get_left(), self.get_lower())
	
	def get_lower_right(self):
		return mhat.Vector2(self.get_right(), self.get_lower())
	
	def get_upper_left(self):
		return mhat.Vector2(self.get_left(), self.get_upper())
	
	def get_upper_right(self):
		return mhat.Vector2(self.get_right(), self.get_upper())
	
	def get_position(self):
		return self._position
	
	def get_size(self):
		return self._size
	
	def get_width(self):
		return self._size.get_x()
	
	def get_height(self):
		return self._size.get_y()
	
	def get_area(self):
		return self.get_width() * self.get_height()