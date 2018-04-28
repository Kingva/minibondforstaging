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

        projectId = 238774  # 100799

        invest = 50000
        useCouponArr = '{\"10\": 0, \"30\": 0,\"50\": 0, \"100\": 0, \"300\": 0, \"500\": 1}'
        userPayPassword = 123456
        useIncreaseCouponArr = '{\"0.50\":1}'  # \
        sid = '2j192bn89d6knj9mv9tsbsdmtt'
        cookie = 'UM_distinctid=1628902cb7c95-0ca21297a6de35-b34356b-100200-1628902cb7d2b; CNZZDATA1253692730=226868447-1522713501-%7C1522724279; kesucorp=2j192bn89d6knj9mv9tsbsdmtt'

        firetime = datetime.combine(
            datetime.now().today(), time(17, 0, 5, 200))
        values = {"projectId": projectId, "num_invest": invest,
                  "useCouponArr": useCouponArr, "useIncreaseCouponArr": useIncreaseCouponArr}

        hdr = {
            'Accept': '*/*',
            'Origin': 'https://www.kesucorp.com',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            # 'Content-Type': 'application/json; charset=UTF-8',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://www.kesucorp.com/project/tenderOrder',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',

            'Cookie': cookie
        }

        # https://www.kesucorp.com/bob/tender?sid=

        beforedata = {"check_agree": "on",
                      "cycle_invest": 30,
                      "dataApr_invest": 8.00,
                      "dataTimeLimit_invest": 180,
                      "fund_invest": 1000.00,
                      "fund_invest": 1000.00,
                      "isPackage": 1,
                      "max_invest": 120000,
                      "num_invest": invest,
                      "projectId": projectId,
                      "repayment_type": 1,
                      "total_invest": 1000000.00,
                      "unitAmount": 100.00}

        needtorequest = True

        pattern = re.compile('"orderId":"(.*?)"', re.S)
        orderid = ""
        print(datetime.now())

        while needtorequest:
            if datetime.now() < firetime:
                # print(str(datetime.now())+"waiting...")
                continue

            print(datetime.now())

            detailurl = "https://www.kesucorp.com/project/detail/" + \
                str(projectId)

            request = urllib.request.Request(
                detailurl,  headers=hdr, method='GET')
            response = urllib.request.urlopen(request)
            response.encoding = 'utf-8'
            print(datetime.now())
            seconds = 2-(datetime.now()-firetime).seconds
            if seconds > 0:
                timetosleep.sleep(seconds)

            needtobefore = True
            while needtobefore:
                beforeurl = "https://www.kesucorp.com/project/beforeTender"
                request = urllib.request.Request(beforeurl, data=urllib.parse.urlencode(
                    beforedata).encode(encoding='UTF8'), headers=hdr, method='POST')
                response = urllib.request.urlopen(request)
                response.encoding = 'utf-8'
                html = response.read().decode('unicode_escape')
                print(html)
                if html.find('false') >= 0:
                    needtobefore = False
                    continue
                else:
                    print(datetime.now())
                    needtobefore = False

            beforesubmiturl = "https://www.kesucorp.com/project/tenderOrder"
            request = urllib.request.Request(
                beforesubmiturl, data=urllib.parse.urlencode(beforedata).encode(encoding='UTF8'), headers=hdr, method='POST')
            response = urllib.request.urlopen(request)
            print(datetime.now())
            response.encoding = 'utf-8'
            print(response)
            html = response.read()
            # print(html)

            seconds = 4-(datetime.now()-firetime).seconds
            if seconds > 0:
                timetosleep.sleep(seconds)

            url = "https://www.kesucorp.com/bob/tender?sid="+sid
            request = urllib.request.Request(
                url, data=urllib.parse.urlencode(values).encode(encoding='UTF8'), headers=hdr, method='POST')
            response = urllib.request.urlopen(request)
            response.encoding = 'utf-8'
            print(response)
            print(datetime.now())
            html = response.read().decode('unicode_escape')
            print(html)
            items = re.findall(pattern, html)
            if len(items) == 1:
                orderid = items[0]
                needtorequest = False
            else:
                continue

            submitvalue = {"orderId": orderid,
                           "userPayPassword": userPayPassword}
            submiturl = "https://www.kesucorp.com/bob/submitTender?sid="+sid
            # https://www.kesucorp.com/bob/submitTender?sid=vdn4ulitb1oqmolb81fmu0nec9
            data = urllib.parse.urlencode(submitvalue).encode(encoding='UTF8')
            needtosubmit = True
            seconds = 6-(datetime.now()-firetime).seconds

            while needtosubmit:
                # print(datetime.now())

                print(seconds)
                if seconds > 0:
                    timetosleep.sleep(seconds)
                request = urllib.request.Request(submiturl, data, headers=hdr)
                response = urllib.request.urlopen(request)
                html = response.read().decode('unicode_escape')
                print(html)
                print(datetime.now())
                needtosubmit = False
                if html.find('"success":true') >= 0:
                    needtosubmit = False
                else:
                    seconds = 1

    except e:
        # logger.info(e)
        print(e)
    finally:
        print('finally...')
        # logger.info("End")
