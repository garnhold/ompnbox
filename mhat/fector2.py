import mhat


class Fector2(mhat.Vector2Base):
	__slots__ = [
		"_x_function",
		"_y_function"
	]
	
	def __init__(self, x_function, y_function):
		super(Fector2, self).__init__()
		
		self._x_function = x_function
		self._y_function = y_function
		
	def get_x(self):
		return self._x_function()
	
	def get_y(self):
		return self._y_function()