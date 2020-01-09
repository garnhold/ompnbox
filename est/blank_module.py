import est

import sys


def blank_module(name):
	sys.modules[name] = est.BlankSurrogate()