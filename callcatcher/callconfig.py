#!/usr/bin/python2
import os.path

cachedir = os.path.expanduser('~/.callcatcher')

def cachefile(file):
	file = os.path.realpath(file)
	file = cachedir + file
	return file
