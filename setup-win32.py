from distutils.core import setup
import py2exe
import os
import shutil

images=[]
version='0.1'
path2src='../../DamnVid/'
description='Converts any damn video to any format. Also supports online video downloading and converting.'
for i in os.listdir(path2src+'img/'):
    if i[-4:].lower()=='.png' or i[-4:].lower()=='.jpg' or i[-4:].lower()=='.gif' or i[-4:].lower()=='.ico' or i[-4:].lower()=='.bmp':
        images.append(path2src+'img/'+i)
class Target:
    def __init__(self,**kw):
        self.__dict__.update(kw)
        self.version=version
        self.company_name='WindPower'
        self.copyright='',
        self.name='DamnVid'

setup(
    name='DamnVid',
    options={
        'py2exe':{
            'compressed':1,
            'optimize':2,
            'ascii':1,
            'bundle_files':1
        }
    },
    zipfile=None,
    version=version,
    description=description,
    author='WindPower',
    author_email='windypower@gmail.com',
    url='http://code.google.com/p/damnvid/',
    windows=[
        {
            'script':path2src+'DamnVid.py',
            'icon_resources':[
                (1,path2src+'img/icon.ico')
            ]
        }
    ],
    data_files=[
        ('output',[path2src+'output/!readme.txt']),
        ('temp',[path2src+'temp/!readme.txt']),
        ('bin',[path2src+'bin/ffmpeg.exe',path2src+'bin/SDL.dll']),
        ('img',images),
        ('conf',[path2src+'conf/!readme.txt',path2src+'conf/conf.ini',path2src+'conf/default.ini'])
    ]
)
shutil.copyfile(path2src+'DamnVid.exe.manifest','dist/DamnVid.exe.manifest')
shutil.copyfile('C:\\Python25\\lib\\site-packages\\wx-2.8-msw-unicode\\wx\\gdiplus.dll','dist/gdiplus.dll')
