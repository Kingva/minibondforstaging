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
        projectId = '41cf896bdf4240068dd31884ab777903'
        invest = 10500
        useCouponArr = '6187359,6187357' #6187359,6187357
        token = ''
        firetime = datetime.now()+timedelta(minutes=3, seconds=20)
        cookie = 'acw_tc=AQAAANJfu3L1ogoAQ0RrJ0njQt0cEbSN; UM_distinctid=1626006eebb543-0d9cc45ed009d6-27d1534-100200-1626006eebc51e; firstEnterUrlInSession=https%3A//www.zhaoshangdai.com/; VisitorCapacity=1; pageReferrInSession=https%3A//ssl.zhaoshangdai.com%3A1000/cas/login%3Ftarget_type%3DP2p%26loginType%3DWEB%26service%3Dhttps%253A%252F%252Fwww.zhaoshangdai.com%253A443%252Fborrow%252Ftender.html%253Fid%253D02a4829444024d2586afef82fe57bc8d; _jzqckmp=1; _jzqx=1.1522032162.1522203010.2.jzqsr=ssl%2Ezhaoshangdai%2Ecom:1000|jzqct=/cas/login.jzqsr=zhaoshangdai%2Ecom|jzqct=/index%2Ehtml; JSESSIONID=PDJqXrQ9ozstP1F5dwSDxBW0K0rUT4YYJvROUvGbej2GfWtaRgf2!2055687269; Hm_lvt_72da47e93f114fd22a380c72f142d731=1522029490; Hm_lpvt_72da47e93f114fd22a380c72f142d731=1522204186; CNZZDATA5451485=cnzz_eid%3D238975068-1522024457-%26ntime%3D1522202798; _qzja=1.683279957.1522029490532.1522200745236.1522203009726.1522203053499.1522204186169..0.0.14.4; _qzjb=1.1522203009725.4.0.0.0; _qzjc=1; _qzjto=8.2.0; _jzqa=1.1693893931344603400.1522029491.1522200745.1522203010.4; _jzqc=1; __utmt=1; __utma=50495714.1961175473.1522029490.1522200745.1522203010.4; __utmb=50495714.4.10.1522203010; __utmc=50495714; __utmz=50495714.1522032162.2.2.utmcsr=ssl.zhaoshangdai.com:1000|utmccn=(referral)|utmcmd=referral|utmcct=/cas/login; _jzqb=1.4.10.1522203010.1'

        data = {}

        
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
        print(url)

        needtorequest = True

        pattern = re.compile("token='(.*?)'", re.S)
        orderid = ""

        while needtorequest:
            if datetime.now() < firetime:
                # print(firetime)
                continue

            print(datetime.now())

            request = urllib.request.Request(
                url,  headers=hdr, method='GET')
            response = urllib.request.urlopen(request)
            # response.encoding = 'utf-8'
            print(response)
            html = response.read().decode()
            # print(html)
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
                if html.find('false') >= 0:
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
