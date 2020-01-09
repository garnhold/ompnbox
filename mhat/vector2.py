import mhat
import collections


class Vector2(mhat.Vector2Base):
	__slots__ = [
		"_x",
		"_y"
	]
	
	def __init__(self, x=0.0, y=0.0):
		super(Vector2, self).__init__()
		
		if isinstance(x, collections.Sized) and len(x) == 2:
			self._x = x[0]
			self._y = x[1]
		else:
			self._x = x
			self._y = y
		
	def get_x(self):
		return self._x
	
	def get_y(self):
		return self._y