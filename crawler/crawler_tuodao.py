import urllib.request
import re
import os
import sys
import urllib3
import json
import http.cookiejar
from time import *

from datetime import *

if __name__ == "__main__":
    try:
        jsessionid=""

        # cookiestr = 'returnUrlEva=%2Fuc; JSESSIONID={};UM_distinctid=1618f98afe3216-0b698c467cd73d-27d1534-240000-1618f98afe47b1; CNZZDATA1256118936=1426011943-1521115175-https%253A%252F%252Fwww.51tuodao.com%252F%7C1521263156; '
        cookiestr='username=18410940187; errortimes=0; UM_distinctid=16305aa23bf0-0a867c007e1e5f-27d1534-100200-16305aa23c02d8; JSESSIONID=5EB5A118FCB205BB12BAB6FAEFACFABC; _fmdata=iK8fwUDSOv7gbstUpsTvDefN%2BvgSJScF7EINk4TyN%2BOXoTAg9HU4LvT0A0bDTGb63set%2BSygMSzK4DQ%2FXNyUL9GsJ4WgtxRx7uV2EUxWbu4%3D; returnUrlEva=%2Fuc; CNZZDATA1256118936=10537479-1524804138-%7C1524804138'

        invest = 34000
        t= urllib.request.quote(str(datetime.now()))#int(datetime.now().timestamp())
        username='18410940187'
        voucherId='2588014'

        password='aa112233'#10d66ccecdf01ccfff2b86cfb1fd2b76
        paypsw='112233'#d0970714757783e6cf17b26fb8e2298f
        
        tenderPwd=''
        data={}
        

        # loginurl='https://www.51tuodao.com/login/login?t={}&userName={}&password=10d66ccecdf01ccfff2b86cfb1fd2b76&verificationCode=remberMe=0&returnUrl='
        # loginurl=loginurl.format(t,username)
        hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
               'Accept': 'application/json, text/javascript, */*; q=0.01',
               # 'Origin': 'https://www.kesucorp.com',
               'X-Requested-With': 'XMLHttpRequest',
               # 'Content-Type': 'application/json; charset=UTF-8',
               'Content-Type': 'application/json',
               'Referer': 'https://www.51tuodao.com/front/login',
               'Accept-Encoding': 'sdch, br',#gzip, deflate, 
               'Accept-Language': 'zh-CN,zh;q=0.8',
               "Connection": "keep-alive",
               'Cookie': cookiestr
               }
        # request = urllib.request.Request(loginurl,  headers=hdr, method='GET')
        
        # cookie = http.cookiejar.CookieJar()  # 声明一个CookieJar对象实例来保存cookie
        # handler = urllib.request.HTTPCookieProcessor(cookie)  # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
        # opener = urllib.request.build_opener(handler)  # 通过handler来构建opener

        # response = opener.open(request)  # 此处的open方法同urllib2的urlopen方法，也可以传入request
        # print(response.read())

        # response = urllib.request.urlopen(loginurl)
        # response.encoding = 'utf-8'
        
        # html = response.read().decode('utf-8')
        # print(html)

        # for item in cookie:
        #     print('Name = ' + item.name)
        #     print('Value = ' + item.value)
        #     if item.name=='JSESSIONID':
        #         jsessionid=item.value
        #         cookiestr=cookiestr.format(jsessionid)
       


        url = "https://www.51tuodao.com/json/borrow/tender?t={}&nid={}&money={}&payPsw=d0970714757783e6cf17b26fb8e2298f&tenderPwd=d41d8cd98f00b204e9800998ecf8427e&quantity={}&baseAmount=NaN&voucherId={}&type=dk&tenderChannel=pc&verificationCode="


        needtorequest = True

        listurl="https://www.51tuodao.com/json/borrow/list2"
        newitempattern= re.compile('<li>.*?id="num_(.*?)".*?仅限新注册用户首次投资.*?个月.*?<i>(.*?)</i>元.*?</li>', re.S)
        listrequest = urllib.request.Request(listurl,  headers=hdr, method='GET')
        

        while needtorequest:

            
            minute=datetime.now().minute

            if minute not in[59,0,1]:
                print(datetime.now())            
                sleep(1)
                continue


            
            response = urllib.request.urlopen(listrequest)
            response.encoding = 'utf-8'
            print(response)
            html = response.read().decode('utf-8')
            # print(html)
            items = re.findall(newitempattern, html)
            for item in items:
                pid=item[0]
                restinvest =float(item[1].replace(",",""))
                print(pid)
                print(restinvest)
                if restinvest > invest:
                    submiturl=url.format(t,pid,invest,restinvest,voucherId)
                    print(submiturl)
                    request = urllib.request.Request( submiturl, headers=hdr, method='GET')
                    response = urllib.request.urlopen(request)
                    response.encoding = 'utf-8'
                    print(response)
                    html = response.read().decode('utf-8')
                    print(html)
                    if html.find('"flag":true')>0:
                        needtorequest=False
                        break


                

            
            # if len(items) == 1:
            #     orderid = items[0]
            #     needtorequest = False

        # submitvalue = {"orderId": orderid, "userPayPassword": userPayPassword}
        # submiturl = "https://www.kesucorp.com/bob/submitTender?sid="+sid
        # data = urllib.parse.urlencode(submitvalue).encode(encoding='UTF8')
        # needtorequest = True
        # request = urllib.request.Request(submiturl, data, headers=hdr)

        # while needtorequest:
        #     response = urllib.request.urlopen(request)
        #     html = response.read().decode('unicode_escape')
        #     print(html)
        #     if html.index('"success":true') >= 0:
        #         needtorequest = False

    except e:
        # logger.info(e)
        print(e)
    finally:
        print('finally...')
        # logger.info("End")
