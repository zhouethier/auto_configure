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

def change_owner (path):
	try:
		command = 'chown -R eplaya:eplaya ' + path
		os.popen("sudo -S %s"%(command), 'w').write('yourmama\n') 
		print "change ownership on Directory: ", command
	except OSError as exception:
		print "Directory ", path, " already exist."
		if exception.errno != errno.EEXIST:
			raise

def change_mod (path):
	try:
		command = 'chmod -R a+wx ' + path
		os.popen("sudo -S %s"%(command), 'w').write('yourmama\n') 
		print "change permission on Directory: ", command
	except OSError as exception:
		print "Directory ", path, " already exist."
		if exception.errno != errno.EEXIST:
			raise

create_path ('/usr/local/ePlaya');
create_path ('/usr/local/ePlaya/bin');
create_path ('/usr/local/ePlaya/lib');

change_owner ('/usr/local/ePlaya');

change_mod('/usr/local/ePlaya');

