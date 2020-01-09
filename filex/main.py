import filex

import glob
import flect
import helpers


def fetch_file(filename, read_provider="Delayed", write_provider="Buffered"):
	return helpers.get_or_create_by_key(
		fetch_file.files, 
		read_provider + "$" + write_provider + "$" + filename, 
		lambda k: filex.File(
			filename,
			flect.instance_subclass_by_suffix(filex.FileReadProvider, read_provider, filename),
			flect.instance_subclass_by_suffix(filex.FileWriteProvider, write_provider, filename)
		)
	)
	
fetch_file.files = {}


def fetch_directory_contents(directory=""):
	return glob.glob(directory + "*")