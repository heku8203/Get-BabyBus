import os
import re
import shutil

path="Y:\Temp\JAV_output"

for root, dirs, files in os.walk(path):
    for d in dirs:
        for f in files:
            file_text = os.path.splitext(f)[-1]
            # print(f)
            if file_text in ('.nfo'):
                # print(dir)
                # f = open(os.path.join(root,f), 'r', encoding='UTF-8')
                with open(os.path.join(root, f), 'r', encoding='UTF-8') as fole:
                    if '无码' in fole.read():
                        pass
                        # print("True")
                    else:
                        pa = os.path.dirname(os.path.join(root, f))
                        print(pa)
                        dir_name = os.path.basename(pa)
                        # print(dir_name)
                        dstpath = 'Y:\Temp\mark\\' + dir_name
                        # os.rename(pa,dstpath)
                        if os.path.exists(dstpath):
                            print("exists")
                        else:
                            # shutil.move(pa, dstpath)
                            print(dstpath)

