import urllib.request
import re
import os
import sys
import urllib3
import json

from datetime import *

if __name__ == "__main__":
    try:
        # useCouponArr:{"10":1,"30":1,"50":4,"100":2,"300":1}
        # useIncreaseCouponArr:{"0.50":1}
        projectId = 236490
        invest = 50000
        useCouponArr = '{\"10\": 4, \"30\": 2,\"50\": 2, \"100\": 0, \"300\": 1, \"500\": 0}'
        userPayPassword = 111111
        useIncreaseCouponArr = '{\"1.00\":1}'
        sid = 'vgfvfg9fja9daq8060d00jvv72'
        firetime = datetime.now()+timedelta(minutes=0, seconds=0)
        cookie = 'kesucorp=vgfvfg9fja9daq8060d00jvv72; UM_distinctid=162474daed64c9-0a3f893ef61b93-27d1534-100200-162474daed74a1; CNZZDATA1253692730=1925229646-1521614504-%7C1521614504'

        values = {"projectId": projectId, "num_invest": invest,
                  "useCouponArr": useCouponArr, "useIncreaseCouponArr": useIncreaseCouponArr}

        data = urllib.parse.urlencode(values).encode(encoding='UTF8')

        print(data)
        hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
               'Accept': '*/*',
               'Origin': 'https://www.kesucorp.com',
               'X-Requested-With': 'XMLHttpRequest',
               # 'Content-Type': 'application/json; charset=UTF-8',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Referer': 'https://www.kesucorp.com/project/tenderOrder',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               "Connection": "keep-alive",
               'Cookie': cookie
               }

        url = "https://www.kesucorp.com/bob/tender?sid="+sid

        needtorequest = True

        pattern = re.compile('"orderId":"(.*?)"', re.S)
        orderid = ""

        while needtorequest:
            if datetime.now() < firetime:
                # print(str(datetime.now())+"waiting...")
                continue

            print(datetime.now())

            request = urllib.request.Request(
                url, data=data, headers=hdr, method='POST')
            response = urllib.request.urlopen(request)
            response.encoding = 'utf-8'
            print(response)
            html = response.read().decode('unicode_escape')
            print(html)
            items = re.findall(pattern, html)
            if len(items) == 1:
                orderid = items[0]
                needtorequest = False

        submitvalue = {"orderId": orderid, "userPayPassword": userPayPassword}
        submiturl = "https://www.kesucorp.com/bob/submitTender?sid="+sid
        data = urllib.parse.urlencode(submitvalue).encode(encoding='UTF8')
        needtorequest = True
        request = urllib.request.Request(submiturl, data, headers=hdr)

        while needtorequest:
            response = urllib.request.urlopen(request)
            html = response.read().decode('unicode_escape')
            print(html)
            if html.find('"success":true') >= 0:
                needtorequest = False

    except e:
        # logger.info(e)
        print(e)
    finally:
        print('finally...')
        # logger.info("End")
