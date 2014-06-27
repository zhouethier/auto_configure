#!/usr/bin/python

import os
import errno

print "Hello World!"

sudoPassword = 'yourmama\n'

def create_path (path):
	try:
		command = 'mkdir ' + path
		os.popen("sudo -S %s"%(command), 'w').write('yourmama\n') 
		print "Make Directory: ", command
	except OSError as exception:
		print "Directory ", path, " already exist."
		if exception.errno != errno.EEXIST:
			raise


#def change_mode (directory) :

create_path ('/usr/local/ePlaya');
create_path ('/usr/local/ePlaya/bin');
create_path ('/usr/local/ePlaya/lib');

#command = 'mkdir /usr/local/ePlaya'
#os.popen("sudo -S %s"%(command), 'w').write('yourmama\n')
