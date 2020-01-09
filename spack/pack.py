#import spack

import mhat
import enumerable


def find_best_box(size, boxs):
	lowest_margin = mhat.POSITIVE_INFINITY
	lowest_margin_box = None
	
	for box in boxs:
		width_margin = box.get_width() - size.get_x()
		height_margin = box.get_height() - size.get_y()
		
		if width_margin >= 0 and height_margin >= 0:
			if width_margin < lowest_margin:
				lowest_margin = width_margin
				lowest_margin_box = box
				
			if height_margin < lowest_margin:
				lowest_margin = height_margin
				lowest_margin_box = box 
				
	return lowest_margin_box, lowest_margin


def find_best_box_and_size(size, boxs, can_flip=False):
	box, margin = find_best_box(size, boxs)
	
	if can_flip:
		flip_size = size.get_swapped()
		flip_box, flip_margin = find_best_box(flip_size, boxs)
		
		if flip_margin < margin:
			size = flip_size
			box = flip_box
			margin = flip_margin
			
	return box, size


def pack_sheet(base_rect, to_pack, can_flip=False):
	boxs = [base_rect]
	
	packed_rects = []
	unpacked_rects = []
	
	for packed_rect in enumerable.new(to_pack).sort_descending(lambda p: p.size.get_max()):
		box, size = find_best_box_and_size(packed_rect.size, boxs, can_flip)
		if box:
			boxs.remove(box)
			
			ll, lr, ur, ul = box.quadsect_lower_left_offset(size)
			boxs.extend([lr, ur, ul])
			
			packed_rect.pack(ll)
			packed_rects.append(packed_rect)
		else:
			packed_rect.depack()
			unpacked_rects.append(packed_rect)
			
	return packed_rects, unpacked_rects
			
			
def pack(base_rect, to_pack, can_flip=False):
	sheets = []
	
	while len(to_pack) > 0:
		packed, to_pack = pack_sheet(base_rect, to_pack, can_flip)
		sheets.append(packed)
		
	return sheets