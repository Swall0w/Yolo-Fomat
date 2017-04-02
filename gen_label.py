# -*- coding:utf-8 -*-
import os
from os import path
import random

def check_file(path='./',ext=''):
    _filelist = os.listdir(path)
    ch_e = []
    for _file in _filelist:
        _root, _ext = os.path.splitext(_file)
        if  _ext == ext:
            ch_e.append(_file)
        else:
            pass
    return ch_e


rootpath = path.dirname(path.abspath(__file__)) + '/'
#imagepaths = os.listdir(rootpath+'dataset')
path = rootpath + 'dataset'
imagepaths = check_file(path=path, ext='.jpg')
print(imagepaths)
val = random.sample(imagepaths,int(len(imagepaths)/5))
train = imagepaths
for item in val:
    train.remove(item)
with open('train.txt','w')as trainfile:
    for path in train:
        abspath = rootpath+'dataset/'+path+'\n'
        trainfile.write(abspath)

with open('val.txt','w')as valfile:
    for path in val:
        abspath = rootpath+'dataset/'+path+'\n'
        valfile.write(abspath)
