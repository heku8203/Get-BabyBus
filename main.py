from pytube import YouTube
import requests
import re
import os
# from pytube.cli import on_progress
import time
# import shutil
# from smb.SMBConnection import SMBConnection
# from smb.base import SharedDevice
# from tqdm import tqdm
def getNameId():
    f=open('url.html','r',encoding='UTF-8')
    # f = tybabybus.text
    # pattern = r'{"videoIds":.*?,'
    pattern = r'{"accessibilityData":{"label":.*?","'
    result = re.findall(pattern, f.read(), re.S)
    ytname=[]
    ytid=[]
    # print(result)
    for r in result:
        if "SHIFT" in str(r) or "hotkeyDialogSectionRenderer" in str(r):
            r='test'
            # print(r)
        pattern1 = r'videoId(.*?),'
        videoId = re.findall(pattern1, r)
        pattern2 = r'label":(.*?)\+'
        name=re.findall(pattern2, r)

        if len(name) !=0:
            name=str(name).replace(r'"','').replace("'",'').replace('[','').replace(']','').replace(':','')
            # print(name)
            ytname.append(name)
        if len(videoId)!=0:
            videoId=str(videoId).replace(r'"','').replace("'",'').replace('[','').replace(']','').replace(':','')
            # print(videoId)
            ytid.append(videoId)
    print(len(ytname),ytname)
    logger(ytname)
    print(len(ytid),ytid)
def getid(ytweb):
    # request网站内容
    tybabybus = requests.get(ytweb)
    print('连接Youtube状态：', tybabybus.status_code)
    logger(tybabybus.status_code)
    # 获取文本
    f=tybabybus.text
    # 提取id
    pattern = r'{"videoIds":.*?,'
    result = re.findall(pattern, f,re.S)
    # 拼接id成下载链接
    urllink=[]
    # urllink = [num for row in result for num in row]
    for r in result:
        # print(r)
        r=r.replace(r'"],','').replace('{"videoIds":["','')
        urllink.append(r)
    # link='https://www.youtube.com/watch?v='+urllink[0]
    return urllink
def Download(link,path):
    youtubeObject = YouTube(link)
    print("文件名称:",youtubeObject.title)

    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        if not os.path.exists(youtubeObject.title+'.mpe'):
            print('预计下载文件大小',round(youtubeObject.filesize/1024/1024,2),'MB')
            logger(round(youtubeObject.filesize/1024/1024,2))
            youtubeObject.download(path)
            print('下载完成')
            logger('下载完成')
            return 0
        else:
            print('目标文件已存在')
            logger('目标文件已存在')
            return 1
    except:
        print("An error has occurred")
        return 1
    print("Download is completed successfully")
# def remove_emoji(text):
#     emoji_pattern = re.compile("["
#                                u"\U0001F600-\U0001F64F"  # emoticons
#                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
#                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#                                # u"\U00002702-\U000027B0"
#                                # u"\U000024C2-\U0001F251"
#                                "]+", flags=re.UNICODE)
#     return emoji_pattern.sub(r'', text)
def filter_str(desstr, restr=''):
    # 过滤除中英文及数字以外的其他字符
    res = re.compile("[^\\u4e00-\\u9fa5^a-z^A-Z^0-9]")
    return res.sub(restr, desstr)
def chagname(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            file_text = os.path.splitext(f)[-1]
            # print(file_text)
            if file_text in ('.mp4','.m4a' ,'.jpg' , '.txt','.srt','.opus','.webm','.mkv'):
                newname = filter_str(f)
                newname=newname.replace("更多",'_').replace("BabyBus寶寶巴士",'').replace("KidsSong",'')
                # newname = remove_emoji(f)
                # newname = re.sub('\【.*?\】','',newname)
                # newname = re.sub('\★.*?\★', '', newname)
                # newname = re.sub('\「.*?\」', '', newname)
                # newname = re.sub('\_[a-zA-Z].*?\_', '', newname)  # 去除英文内容
                # newname = re.sub('\(.*?\)', '', newname)  # 去除括号和里面内容
                # newname = newname.replace('寶寶巴士', '').replace('宝宝巴士', '').replace('BabyBus', '').replace('_卡通片','').replace(
                #     '+更多', '_').replace('_合集', '').replace('_片', '').replace('片片','').replace(' ', '').replace('_.', '.').replace('__', '_').replace('__', '_').replace('＋更多合集','')
                # newname = newname.replace('douyin', '').replace('❤️ZinnZinn','')
                srcname=os.path.join(root,f)
                dstname=path+'\\'+newname
                print('新文件名:',dstname)
                logger(dstname)
                if srcname != dstname:
                    if not os.path.exists(dstname):
                        # print('可以修改')
                        os.rename(srcname,dstname)  ##$#!!!!谨慎
                    else:
                        print('目标文件已存在')
                        # os.rename(srcname, "Y:\巴士回收\\" + f)
            else:
                # os.remove(srcname)
                continue
    print("重命名完毕")
    logger("重命名完毕")
def category(filename):
    if '安全警長啦咘啦哆' in filename:
        return '安全警長啦咘啦哆'
    elif '安全' in filename :
        return '安全儿歌'
    elif '奇妙救援隊' in filename :
        return '奇妙救援隊'
    elif '美食' in filename:
        return '美食家族'
    elif '漢字' in filename:
        return '奇妙漢字'
    elif '奇奇' in filename or '妙妙' in filename:
        return '奇奇妙妙'
    elif '车' in filename or '車' in filename:
        return '交通工具'
    elif '兒歌' in filename or '儿歌' in filename or '童謠' in filename:
        return '儿歌童谣'
    elif '小猪佩奇' in filename:
        return '小猪佩奇'
    else:
        return "其他"
def move_files(path,dst):
    for root, dirs, files in os.walk(path):
        for f in files:
            file_text = os.path.splitext(f)[-1]
            if file_text in ('.mp4','.m4a' ,'.jpg' , '.txt','.srt','.opus','.webm','.mkv'):
                folder=dst+'\\'+category(f)+'\\'
                if not os.path.exists(folder):
                    os.mkdir(folder)
                srcpath=os.path.join(root,f)
                dstpath=folder+f
                if not os.path.exists(dstpath):
                    print('准备移动到'+dstpath)
                    os.rename(srcpath,dstpath)
                else:
                    if not os.path.exists("Y:\巴士回收\\"+f):
                        print('文件已存在,移动回收站:'+dstpath)
                        os.rename(srcpath, "Y:\巴士回收\\"+f)
                    else:
                        print('回收站重复,删除文件'+dstpath)
                        # os.remove(dstpath)
    print('分类文件完成')
    logger('分类文件完成')
def logger(msg):
    global logs
    logs.append(msg)

if __name__ == '__main__':
    # 配置youtube路径
    # ytChannel='https://www.youtube.com/channel/UCttafJi4SCirZhlxsxISbyA'
    ytweb='http://www.youtube.com/@BabyBusTC/videos'
    # 目的路径
    dst_path = r'Y:\Media\儿童\宝宝巴士Youtube'
    # 下载路径
    path=r'Y:\youtube'
    # yt = YouTube('https://www.youtube.com/watch?v=cowy1pou3QY')
    # 从网站获取更新
    logs=[]
    onlinelist=getid(ytweb)
    # print(onlinelist)
    读取本地已下载记录
    loclist=open('id_download_log.csv', 'r', encoding='UTF-8').read().replace('[','').replace(']','').replace("'",'').replace(',','').split()
    # 开始下载并更新本地记录
    for id in onlinelist:

        if id not in loclist:
            logger(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print('开始下载:',id)
            logger(id)
            d=Download('https://www.youtube.com/watch?v='+id,path)
            loclist.append(id)
            if d == 0:
                f = open('id_download_log.csv', 'w', encoding='UTF-8')
                f.write(str(loclist))
                print('本地数据已更新')
                logger('以下载 \n')
                f.close()

                f = open('logs.csv', 'a', encoding='UTF-8')
                f.write(str(logs))
                f.write('\n')
                f.close()
        else:
            # print('没有发现新文件')
            # logger('没有发现新文件')
            continue

    # 格式化文件名
    chagname(path)
    # 移动文件
    move_files(path,dst_path)

    # print(logs)



    # https://www.youtube.com/watch?v=xkWVlhX3rM0
    # yt=YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
    # yt=YouTube('https://www.youtube.com/watch?v=cowy1pou3QY')
    # get_Channel(ytChannel)
    # ytweb='https://m.youtube.com/@BabyBusTC/videos'
    # tybabybus = requests.get(ytvideo)
    # 查看状态码
    # print('状态码：', tybabybus.status_code)
    # print('cookies',tybabybus.cookies)
    # print('查看网页内容：', tybabybus.text)


    # yt=YouTube(getid(ytweb))

    # yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
    # for t in yt.streams:
    #     print('可选',t)
    # # yt = yt.streams.get_highest_resolution()
    # itag=str(yt)
    # yt=yt.streams.filter(adaptive=True)
    # print(yt)
    # yt = yt.streams.get_highest_resolution()
    # # print(yt.streams)
    # yt.download()
    # yt.streams.filter(adaptive=True)
    # Download(yt)


    # 获取网页内容
    # tybabybus = requests.get(ytweb)
    # print('状态码：', tybabybus.status_code)
    # # 将网页保存为文件
    # f=open('url.html', 'w', encoding='UTF-8')
    # f.write(tybabybus.text)
    # f.close()

    # urllink = []
    # for r in result:
    #     # print(r)
    #     r = r.replace(r'"],', '').replace('{"videoIds":["', '')
    #     urllink.append(r)
    # link = 'https://www.youtube.com/watch?v=' + urllink[0]


