#2015年8月15日 22:36:26
#爬取百度贴吧 正则表达式

import urllib.request
import re

#url = input('请输入您需要爬取的百度贴吧的地址：')
url = 'http://tieba.baidu.com/p/3977180464'
#url = 'http://tieba.baidu.com/p/3974556969'
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

#加了括号，所以打印出来的内容只有括号里面的
p = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>')
items = p.findall(html)
for item in items:
    print(item)
#打印出作者的ID
p = re.compile('<a.*?class="p_author_name.*?>(.*?)</a>')
items = p.findall(html)
for item in items:
    print(item)

'''
p = re.compile('<div id="post_content_.*?>(.*?)</div>')
items = p.findall(html)

def replace(items):   
    removeImg = re.compile('<img.*?>')
    removeAddr = re.compile('<a.*?>|</a>')
    removeLine = re.compile('<tr>|<div>|</div>|</p>|<td>|<br>')
    items = re.sub(removeImg, '', items)
    items = re.sub(removeAddr, '', items)
    items = re.sub(removeLine, '', items)
    items = items.strip()
    return items

for item in items:
    item = replace(item)
    #print('这是第', floor, '楼---------------')
    print(item)
    floor = floor + 1
'''
