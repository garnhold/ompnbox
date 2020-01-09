import prof


METHOD_INSTANCE_STACK = [
	prof.MethodInstance(None, None)
]

def render():
	return prof.METHOD_INSTANCE_STACK[0].render()