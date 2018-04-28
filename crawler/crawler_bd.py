import urllib.request
import re
import os
import sys
import urllib3
import json
import random
from datetime import *
import time as timetosleep


if __name__ == "__main__":
    try:
        # useCouponArr:{"10":1,"30":1,"50":4,"100":2,"300":1}
        # useIncreaseCouponArr:{"0.50":1}

        hdr = {
            'Accept': '*/*',
            'Origin': 'https://www.baidu.com',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            # 'Content-Type': 'application/json; charset=UTF-8',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://www.kesucorp.com/project/tenderOrder',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',

            # 'Cookie': cookie
        }

        needtorequest = True

        pattern = re.compile('window.location.replace\("(.*?)"\)', re.S)
        url = ""
        print(datetime.now())
# https://www.baidu.com/link?url=NtKBtTGuGGFWfslYt5Y4hm6uQ7HlPLsF2KZDPT2T_LVT9AU05KRUkC6qQi8iRxYgUrfHgVw6tjzeE-S9ffH4Sa&wd=&eqid=979487a3000072c2000000035ad95b03
        beforeurl = "http://www.baidu.com/link?url=EEesF7FF_jy_5YkQb0ZB1S4s_5gMOpmX-YLRoLw5022T3FIVQ-WaMZ3JSvBlwo3NrL2--T4LSU63ONopvZ_gum_uz--UBj80MJeoqS0LtyW"
        request = urllib.request.Request(beforeurl, headers=hdr, method='GET')
        response = urllib.request.urlopen(beforeurl)
        print(response)
        response.encoding = 'utf-8'
        html = response.read().decode('utf-8')
        print(html)
        items = re.findall(pattern, html)
        if len(items) > 0:
            url = items[0]
            print(url)
        else:
            print(items)
            "continue"

        # while needtorequest:
        #     if datetime.now() < firetime:
        #         # print(str(datetime.now())+"waiting...")
        #         continue

        #     print(datetime.now())

        #     detailurl = "https://www.kesucorp.com/project/detail/" + \
        #         str(projectId)

        #     needtobefore = True
        #     while needtobefore:
        #         beforeurl = "https://www.kesucorp.com/project/beforeTender"
        #         request = urllib.request.Request(beforeurl, data=urllib.parse.urlencode(
        #             beforedata).encode(encoding='UTF8'), headers=hdr, method='POST')
        #         response = urllib.request.urlopen(request)
        #         response.encoding = 'utf-8'
        #         html = response.read().decode('unicode_escape')
        #         print(html)
        #         if html.find('false') >= 0:
        #             needtobefore = False
        #             continue
        #         else:
        #             print(datetime.now())
        #             needtobefore = False

        #     beforesubmiturl = "https://www.kesucorp.com/project/tenderOrder"
        #     request = urllib.request.Request(
        #         beforesubmiturl, data=urllib.parse.urlencode(beforedata).encode(encoding='UTF8'), headers=hdr, method='POST')
        #     response = urllib.request.urlopen(request)
        #     print(datetime.now())
        #     response.encoding = 'utf-8'
        #     print(response)
        #     html = response.read()
        #     # print(html)

        #     seconds = 3-(datetime.now()-firetime).seconds
        #     if seconds > 0:
        #         timetosleep.sleep(seconds)

        #     url = "https://www.kesucorp.com/bob/tender?sid="+sid
        #     request = urllib.request.Request(
        #         url, data=urllib.parse.urlencode(values).encode(encoding='UTF8'), headers=hdr, method='POST')
        #     response = urllib.request.urlopen(request)
        #     response.encoding = 'utf-8'
        #     print(response)
        #     print(datetime.now())
        #     html = response.read().decode('unicode_escape')
        #     print(html)
        #     items = re.findall(pattern, html)
        #     if len(items) == 1:
        #         orderid = items[0]
        #         needtorequest = False
        #     else:
        #         continue

        #     submitvalue = {"orderId": orderid,
        #                    "userPayPassword": userPayPassword}
        #     submiturl = "https://www.kesucorp.com/bob/submitTender?sid="+sid
        #     # https://www.kesucorp.com/bob/submitTender?sid=vdn4ulitb1oqmolb81fmu0nec9
        #     data = urllib.parse.urlencode(submitvalue).encode(encoding='UTF8')
        #     needtosubmit = True
        #     seconds = 3-(datetime.now()-firetime).seconds

        #     while needtosubmit:
        #         # print(datetime.now())

        #         print(seconds)
        #         if seconds > 0:
        #             timetosleep.sleep(seconds)
        #         request = urllib.request.Request(submiturl, data, headers=hdr)
        #         response = urllib.request.urlopen(request)
        #         html = response.read().decode('unicode_escape')
        #         print(html)
        #         print(datetime.now())
        #         needtosubmit = False
        #         if html.find('"success":true') >= 0:
        #             needtosubmit = False
        #         else:
        #             seconds = 1

    except e:
        # logger.info(e)
        print(e)
    finally:
        print('finally...')
        # logger.info("End")
