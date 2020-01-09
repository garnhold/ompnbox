import log


LOGGER = log.Logger_Print()


def indent():
	get_logger().indent()
	
	
def dedent():
	get_logger().dedent()


def message(message):
	get_logger().log_message(message)
	
	
def error(message):
	get_logger().log_error(message)
	
	
def exception():
	get_logger().log_exception()
	
	
def set_logger(new_logger):
	global LOGGER
	LOGGER = new_logger
	
	
def get_logger():
	return LOGGER