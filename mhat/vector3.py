import mhat


class Vector3(mhat.Vector3Base):
	__slots__ = [
		"_x",
		"_y",
		"_z"
	]
	
	def __init__(self, x=0.0, y=0.0, z=0.0):
		super(Vector3, self).__init__()
		
		if len(x) == 3:
			self._x = x[0]
			self._y = x[1]
			self._z = x[2]
		else:
			self._x = x
			self._y = y
			self._z = z
		
	def get_x(self):
		return self._x
	
	def get_y(self):
		return self._y
	
	def get_z(self):
		return self._z