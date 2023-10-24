from mutagen.flac import FLAC
import os
import re
from zhconv import convert

def readflac(file):
    try:
        audio = FLAC(file)
    finally:
        pass
        # os.remove(file)
    # a=audio.pprint()
    title = audio.get("title", "Unknown Title")
    artist = audio.get("artist", "Unknown Artist")
    tag=[]
    tag.append(title)
    tag.append(artist)
    tag = [num for row in tag for num in row]
    return tag
def FileName(STR):
    for i,j in ("/_","\\_","?_","|︱","\"_","*＊","<＜",">＞",":_",",_","＼_"):
        STR=STR.replace(i,j).replace(' ','').replace('...','').replace(' ','')
    return STR
def filter_str(desstr, restr=''):
    # 过滤除中英文以外的其他字符
    res = re.compile("[^\\u4e00-\\u9fa5^a-z^A-Z]")
    return res.sub(restr, desstr)

path=r'W:\TBD'
dst=r'W:\2023music'
for root, dirs, files in os.walk(path):
    for f in files:
        file_text = os.path.splitext(f)[-1]
        if file_text in ('.flac') :
            pa = os.path.join(root,f)
            tag=readflac(pa)
            tag[0] = FileName(tag[0])
            tag[1] = filter_str(tag[1])
            tag[1] = FileName(tag[1])
            tag[0]=convert(tag[0], 'zh-cn')
            tag[1]=convert(tag[1], 'zh-cn')
            if tag[1] is None:
                tag[1]="Unknown Title"
            # if tag[1]:
            #     tag[1] = "Unknown Artist"
            folder = dst + '\\'+tag[1]
            dstpath=folder+"\\"+tag[0]+'-'+tag[1]+file_text
            print('准备从',pa,'移动到',dstpath)
            # print(tag)
            if not os.path.exists(folder):
                os.mkdir(folder)
            else:
                if not os.path.exists(dstpath):
                    try:
                        os.rename(pa,dstpath)
                    except FileNotFoundError:
                        # os.remove(pa)
                        pass
                else:
                    print('目标已存在',pa)
                    os.remove(pa)
                    pass
        else:
            pass
