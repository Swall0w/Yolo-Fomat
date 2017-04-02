from PIL import Image
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

jpglist = check_file(path='dataset', ext='.jpg')

for jpg in jpglist:
    im = Image.open('dataset/'+jpg)
    imX, imY = im.size
    if imX <=448 or imY <= 448:
        print(jpg, imX, imY)
        os.remove('dataset/'+jpg)
        os.remove('dataset/'+os.path.splitext(jpg)[0] + '.txt')

