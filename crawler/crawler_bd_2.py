import urllib.request
import re
import os
import sys
import urllib3
import json
import random
from datetime import *
import time as timetosleep
import string
from discuz import *


def getSourceUrl(beforeurl):
    pattern = re.compile('window.location.replace\("(.*?)"\)', re.S)

    request = urllib.request.Request(beforeurl, headers=hdr, method='GET')
    response = urllib.request.urlopen(beforeurl)
    response.encoding = 'utf-8'
    html = response.read().decode('utf-8')

    items = re.findall(pattern, html)
    if len(items) > 0:
        beforeurl = items[0]

    return beforeurl


def replaceCharEntity(htmlStr):
    ''''' 
    替换html中常用的字符实体 
    使用正常的字符替换html中特殊的字符实体 
    可以添加新的字符实体到CHAR_ENTITIES 中 
CHAR_ENTITIES是一个字典前面是特殊字符实体  后面是其对应的正常字符 
    :param htmlStr: 
    '''

    CHAR_ENTITIES = {'nbsp': ' ', '160': ' ',
                     'lt': '<', '60': '<',
                     'gt': '>', '62': '>',
                     'amp': '&', '38': '&',
                     'quot': '"''"', '34': '"', }
    re_charEntity = re.compile(r'&#?(?P<name>\w+);')
    sz = re_charEntity.search(htmlStr)
    while sz:
        entity = sz.group()  # entity全称，如>
        # 去除&;后的字符如（" "--->key = "nbsp"）    去除&;后entity,如>为gt
        key = sz.group('name')
        try:
            htmlStr = re_charEntity.sub(CHAR_ENTITIES[key], htmlStr, 1)
            sz = re_charEntity.search(htmlStr)
        except KeyError:
            # 以空串代替
            htmlStr = re_charEntity.sub('', htmlStr, 1)
            sz = re_charEntity.search(htmlStr)
    return htmlStr


if __name__ == "__main__":
    try:
        searchwords = "钱满仓 爆雷"
        pattern = re.compile(
            '<div class="result c-container ".*?<h3.*?href = "(.*?)".*?>(.*?)</a>.*?<div class="c-abstract">(.*?)...</div>', re.S)
        urlpattern = re.compile('<h3.*?href = "(.*?)"', re.S)
        clhtmlpattern = re.compile(r'<[^>]+>', re.S)
        retriver = Retriver("contentxls\content.xlsx", "Sheet1", 2)

        for pn in list(reversed(list(range(0, 110, 10)))):
            beforeurl = u"http://www.baidu.com/s?pn={}&wd={}".format(
                pn, searchwords)
            response = urllib.request.urlopen(
                urllib.parse.quote_plus(beforeurl, safe=string.printable))
            html = response.read().decode('utf-8')
            items = re.findall(pattern, html)
            print(len(items))

            for item in items:
                print("=============================================================")
                url = item[0]
                print(url)
                subject = replaceCharEntity(clhtmlpattern.sub('', item[1]))
                print(subject)
                summary = replaceCharEntity(
                    clhtmlpattern.sub('', item[2])+"......")

                retriver.addPostToList(
                    url, subject[:subject.rfind("_")], summary)

    except e:
        # logger.info(e)
        print(e)
    finally:
        print('finally...')
        # logger.info("End")
