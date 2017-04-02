# -*- coding:utf-8 -*-
import os
import os.path

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

txtlist = check_file(path='./', ext='.txt')
jpglist = check_file(path='./', ext='.jpg')
print(len(txtlist))
print(len(jpglist))
deletelist = []
for jpgfile in jpglist:
    jpg2txt = os.path.splitext(jpgfile)[0] + '.txt'
    if jpg2txt not in txtlist:
        deletelist.append(jpgfile)

for txtfile in txtlist:
    txt2jpg = os.path.splitext(txtfile)[0] + '.jpg'
    if txt2jpg not in jpglist:
        deletelist.append(jpgfile)
##        os.remove(txt2jpg)
print(deletelist)
print('deletelist ',len(deletelist))
#for item in deletelist:
##    os.remove('./'+item)
#    print(item)
        os.remove('dataset/'+jpg)
