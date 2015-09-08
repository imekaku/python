#2015年8月16日 20:46:30
#百度贴吧爬取 正则表达式 网页html爬取
#by imekaku.com

import urllib.request
import re

#url = input('请输入您需要爬取的百度贴吧的地址：')
url = 'http://tieba.baidu.com/p/3975584183'

def openUrl(url):
    #模拟浏览器浏览行为，添加headers
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'
    req = urllib.request.Request(url, headers) 
    #获取网页
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    return html

#替换不必要的字符
def replace(items):   
    removeImg = re.compile('<img.*?>')
    removeAddr = re.compile('<a.*?>|</a>')
    removeLine = re.compile('<tr>|<div>|</div>|</p>|<td>|<br>')
    removeClass = re.compile('<div class=".*?>')
    items = re.sub(removeImg, '', items)
    items = re.sub(removeAddr, '', items)
    items = re.sub(removeLine, '', items)
    items = re.sub(removeClass, '', items)
    items = items.strip()
    return items

html = openUrl(url)
p = re.compile('<div id="post_content_.*?>(.*?)</div>')
items = p.findall(html)
floor = 1

for item in items:
    item = replace(item)
    with open('tieba.txt', 'a') as f:
        floorline = '这个是第' + str(floor) + '楼---------------------\n'
        enterline = '\n\n'
        print(floorline)
        print(item)
        f.write(floorline)
        f.write(item)
        f.write(enterline)
    floor = floor + 1
