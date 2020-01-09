# import filex

import os.path


def delete_internal(filename):
	if os.path.isfile(filename):
		os.remove(filename)


def write_text_internal(filename, text):
	with open(filename, 'w') as text_file:
		text_file.write(text)
		
		
def write_binary_internal(filename, binary):
	with open(filename, 'wb') as binary_file:
		binary_file.write(binary)
			
			
def append_text_internal(filename, text):
	with open(filename, 'a') as text_file:
		text_file.write(text)
			

def read_text_internal(filename):
	with open(filename, 'r') as text_file:
		return text_file.read()
	
	
def read_binary_internal(filename):
	with open(filename, 'rb') as binary_file:
		return binary_file.read()
	
	
def is_file_internal(filename):
	return os.path.isfile(filename)
	
	
def get_size_internal(filename):
	return os.path.getsize(filename)


def get_create_time_internal(filename):
	return os.path.getctime(filename)


def get_last_write_time_internal(filename):
	return os.path.getmtime(filename)