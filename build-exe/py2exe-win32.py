# -*- coding: utf-8 -*-
# This is just a building script for py2exe.

from distutils.core import setup
import py2exe
import os, sys
import shutil

path2src = os.path.abspath(os.path.dirname(sys.argv[0])+os.sep+'..')+os.sep
sys.path.append(path2src)
versionfile = open(path2src + 'version.d', 'r')
version = versionfile.readline().strip()
versionfile.close()
description = 'DamnVid'
files = open(path2src + 'required-files.txt', 'r')
data_files = []
for f in files.readlines():
	curfile = f.strip()
	if curfile and curfile != 'DamnVid.exe':
		if curfile.find(os.sep) == -1:
			data_files.append(path2src + curfile)
		else:
			data_files.append((curfile[:curfile.rfind(os.sep)], [path2src + curfile]))
files.close()
class Target:
	def __init__(self, **kw):
		self.__dict__.update(kw)
		self.version = version
		self.company_name = 'Etienne Perot'
		self.copyright = '',
		self.name = 'DamnVid'

setup(
	name='DamnVid',
	options={
		'py2exe':{
			'compressed':1,
			'optimize':2,
			'ascii':1,
			'bundle_files':3,
			'packages':[
				'encodings'
			]
		}
	},
	zipfile=None,
	version=version,
	description=description,
	author='Etienne Perot',
	author_email='windypower@gmail.com',
	url='http://code.google.com/p/damnvid/',
	windows=[
		{
			'script':path2src + 'DamnVid.py',
			'icon_resources':[
				(0, path2src + 'img/icon.ico')
			]
		}
	],
	data_files=data_files
)
