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
        projectId = 'ea127f31637e4cbca7462758014a3b3a'
        invest = 16500
        useCouponArr = '6187359,6187358,6187357'
        userPayPassword = 111111
        token = ''
        firetime = datetime.now()+timedelta(minutes=0, seconds=0)
        cookie = 'acw_tc=AQAAAPvOwSPyWwgAVsmEOn0Dxu0X06jZ; JSESSIONID=8qRCq0m2qoKjJt0HCg8PtVclyvvjHTUbSSQYwC85HdMQ4oAWgo3K!747367268; UM_distinctid=16242aeaa694f4-09bed02af2c407-5d4e211f-100200-16242aeaa6a369; _jzqckmp=1; firstEnterUrlInSession=https%3A//www.zhaoshangdai.com/; __utmt=1; pageReferrInSession=https%3A//www.zhaoshangdai.com/user/account/detail.html; VisitorCapacity=1; Hm_lvt_72da47e93f114fd22a380c72f142d731=1521537166; Hm_lpvt_72da47e93f114fd22a380c72f142d731=1521537492; CNZZDATA5451485=cnzz_eid%3D1945780577-1521535572-%26ntime%3D1521535572; _jzqa=1.3165847837248408600.1521537166.1521537166.1521537166.1; _jzqc=1; _qzja=1.1466291022.1521537166320.1521537166320.1521537166321.1521537198680.1521537491925..0.0.5.1; _qzjb=1.1521537166321.5.0.0.0; _qzjc=1; _qzjto=5.1.0; _jzqb=1.5.10.1521537166.1; __utma=50495714.1680769850.1521537167.1521537167.1521537167.1; __utmb=50495714.4.10.1521537167; __utmc=50495714; __utmz=50495714.1521537167.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'

        data = {}

        print(data)
        hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
               'Accept': 'text/plain, */*; q=0.01',
               'Origin': 'https://www.zhaoshangdai.com',
               'X-Requested-With': 'XMLHttpRequest',
               # 'Content-Type': 'application/json; charset=UTF-8',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Referer': 'https://www.zhaoshangdai.com/borrow/tender.html?id='+projectId,
               'Accept-Encoding': 'sdch, br',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               "Connection": "keep-alive",
               'Cookie': cookie
               }

        url = 'https://www.zhaoshangdai.com/borrow/tender.html?id='+projectId

        needtorequest = True

        pattern = re.compile("token='(.*?)'", re.S)
        orderid = ""

        while needtorequest:
            if datetime.now() < firetime:
                # print(str(datetime.now())+"waiting...")
                continue

            print(datetime.now())

            request = urllib.request.Request(
                url,  headers=hdr, method='GET')
            response = urllib.request.urlopen(request)
            response.encoding = 'utf-8'
            print(response)
            html = response.read().decode('gbk')
            print(html)
            items = re.findall(pattern, html)
            if len(items) == 1:
                token = items[0]
            else:
                continue

            submitvalue = {"borrowId": projectId, "money": invest,
                           "couponStr": useCouponArr, "token": token}
            submiturl = "https://www.zhaoshangdai.com/tender/tender.html"
            data = urllib.parse.urlencode(submitvalue).encode(encoding='UTF8')
            needtosubmit = True
            request = urllib.request.Request(submiturl, data, headers=hdr)

            while needtosubmit:
                response = urllib.request.urlopen(request)
                html = response.read().decode('utf-8')
                print(html)
                if html.find('"isSuccess":false') >= 0:
                    break

                else:
                    needtorequest = False
                    needtosubmit = False

    except e:
        # logger.info(e)
        print(e)
    finally:
        print('finally...')
        # logger.info("End")
