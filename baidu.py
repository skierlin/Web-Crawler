# https://image.baidu.com/search/index?tn=baidu
# image&ipn=r&ct=201326592&cl=2&lm=-1&st=-
# 1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&
# pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&h
# eight=&face=0&istype=2&ie=utf8&word=desk&oq=desk&rsp=-1

# https://img1.baidu.com/it/u=1300120052,4089645275&fm=253&fmt=auto&app=138&
# f=JPEG?w=800&h=500
import sys
import re
import requests
import chardet


def getHtml2(url):
    fakeHeaders = {'User-Agent':
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                       AppleWebKit/537.36 (KHTML, like Gecko) \ '
                       'Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.77',
                   'Accept': 'text/html,application/xhtml+xml,*/*'}
    try:
        r = requests.get(url, headers=fakeHeaders)
        ecd = chardet.detect(r.content)['encoding']  # ecd是个字符串
        if ecd.lower() != sys.getdefaultencoding().lower():
            r.encoding = ecd  # 修改r中文本的编码
        else:
            r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print(e)
        return ""


def getHtml(url):
    fakeHeaders = {'User-Agent':  # 用于伪装浏览器发送请求
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                       AppleWebKit/537.36 (KHTML, like Gecko) \ '
                       'Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.77',
                   'Accept': 'text/html,application/xhtml+xml,*/*'}
    try:
        r = requests.get(url, headers=fakeHeaders)
        r.encoding = r.apparent_encoding  # 确保网页编码正确
        return r.text  # 返回值是个字符串，内含整个网页内容
    except Exception as e:
        print(e)
    return ""


def getBaiduPic(word, n):
    url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word="
    url += word
    html = getHtml2(url)
    pt = '\"thumbURL\":.*?\"(.*?)\"'  # 正则表达式，用于寻找图片网址
    i = 0

    for x in re.findall(pt, html):  # x就是图片url
        print(x)
        x = x.lower()
        try:
            r = requests.get(x, stream=True)  # 获取x对应的网络资源
            f = open('{0}{1}.jpg'.format(word, i), "wb")
            # "wb"表示二进制写方式打开文件
            f.write(r.content)  # 图片内容写入文件
            f.close()
            i = i + 1
        except Exception as e:
            pass
        if i >= n:
            break


getBaiduPic("猫", 10)
getBaiduPic("熊猫", 10)
