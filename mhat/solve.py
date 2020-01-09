#import mhat


def solve(x1, x2, y, function, margin=0.01):
	y1 = function(x1)
	y2 = function(x2)
	
	if y1 < y2:
		under_y, over_y = y1, y2
		under_x, over_x = x1, x2
	else:
		under_y, over_y = y2, y1
		under_x, over_x = x2, x1
		
	if y < under_y:
		return under_x
	
	if y > over_y:
		return over_x
		
	while True:
		current_x = (under_x + over_x) / 2.0
		current_y = function(current_x)
		
		if current_y < y:
			under_x = current_x
		elif current_y > y:
			over_x = current_x
		else:
			return current_x
		
		if abs(under_x - over_x) < margin:
			break
			
	return current_x
