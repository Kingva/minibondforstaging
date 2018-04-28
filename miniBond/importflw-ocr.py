# # from WindPy import w
import os
import sys
import re
from PIL import Image
from pytesseract import *
import urllib.request

pathname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(pathname, '..')))

# from datetime import *
from django.db import models
from django.conf import settings
import django
from datetime import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 外部调用django时，需要设置django相关环境变量

# 设置INSTALLED_APPS信息
INSTALLED_APPS = [
    'miniBond',
    # 'django.contrib.admin',
]
# 设置数据库信息
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# 给Django配置相关信息
settings.configure(DATABASES=DATABASES, INSTALLED_APPS=INSTALLED_APPS)
# 启动Django
django.setup()

from miniBond.models import *
# from WindPy import w
import logging
import logging.config
import logging.handlers
from datatoimport import *
import uuid

CONF_LOG = "loggingconfig.config"
logging.config.fileConfig(CONF_LOG)  # 采用配置文件
logger = logging.getLogger("fetchinterests")

# class bondTradinfo:


if __name__ == "__main__":

    try:
        listurl = 'http://shop.fanli.com/home/licai/'
        listurl = 'http://shop.fanli.com/Home/licai/ajaxGetUserShops?userid=185331149&t=1514966380691'

        tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR"'

        pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

        agency = PromotionAgency.objects.filter(name="返利网").first()
        promotions = PromotionInfo.objects.filter(promotionAgency=agency)
        promotions.delete()

        # print(pageindex)

        # values = {"currentPage": pageindex}

        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}

        url = listurl
        request = urllib.request.Request(url, headers=hdr)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        # print(html)
# <a class="goto" href="http://shop.fanli.com/home/licai/detail?id=1669" target="_blank" data-spm="licai_home.pc.pty-go~ptid-2244~std-28996">去投资拿返利</a>
        pattern = re.compile('<a class="goto" href="(.*?)"', re.S | re.I)
        items = re.findall(pattern, html)
        for item in range(1, 2):
            # print(item[0])

            # detaillink = item[0]
            detaillink = 'http://shop.fanli.com/home/licai/detail?id=1681'
            print(detaillink)

            request = urllib.request.Request(detaillink, headers=hdr)
            response = urllib.request.urlopen(request)
            detailhtml = response.read().decode('utf-8')
            print(detailhtml)

            # <p class="top-img"><img src="http://l4.51fanli.net/shop/images/2017/12/5a3ced007b9f5.jpg" alt=""></p>

            imgp = re.compile(
                r'<p class="top-img">.*?<img src="(.*?)"', re.S)
            match = re.search(imgp, detailhtml)
            if match:
                print(match.group())

                # bonus = dr.sub('', item[1]).strip().replace(
                #     "\n", "").replace("\r", "")
                # print(''.join(bonus.split(" ")))
                # pfname = re.findall("<span>(.*?)</span>", item[2])[1]

                # platform = Platform.objects.filter(name=pfname).first()

                # if platform and agency:
                #     promotion = PromotionInfo.objects.filter(
                #         platForm=platform, promotionAgency=agency).first()
                #     promotion = promotion if promotion else PromotionInfo()
                #     promotion.url = link
                #     promotion.description = bonus
                #     promotion.platForm = platform
                #     promotion.promotionAgency = agency
                #     promotion.isValid = 1
                #     promotion.save()
                #     platform.isValid = 1
                #     platform.save()
                #     print(platform.name+"+++"+agency.name)

                # else:
                #     print("not found."+pfname)

        # imgurl = 'http://l4.51fanli.net/shop/images/2017/12/5a3ced007b9f5.jpg'
        # filename = '../imgsdownloaded/'+str(uuid.uuid1())+".jpg"

        # urllib.request.urlretrieve(imgurl, filename)

        # text = pytesseract.image_to_string(
        #     Image.open(filename), lang='chi_sim', config=tessdata_dir_config)
        # # print(text)

        # items = text.splitlines()
        # # for item in items:
        # print(''.join(items[-1].split()))
        # print(pfname)

        # pf = "钱多多"
        # url = "http://shop.fanli.com/home/licai/detail?id=1635&spm=licai_home.pc.pty-go~ptid-2210~std-28996"
        # comments = "首次投资最高返利：120元+投资金额x1%"
        # isvalid = 1

        # platform = Platform.objects.filter(name=pf).first()
        # agency = PromotionAgency.objects.filter(name="返利网").first()
        # if platform and agency:
        #     promotion = PromotionInfo.objects.filter(
        #         platForm=platform, promotionAgency=agency).first()
        #     promotion = promotion if promotion else PromotionInfo()
        #     promotion.url = url
        #     promotion.description = comments
        #     promotion.platForm = platform
        #     promotion.promotionAgency = agency
        #     promotion.isValid = isvalid
        #     promotion.save()
        #     platform.isValid = platform.isValid if not isvalid else isvalid
        #     platform.save()
        #     print(platform.name+"+++"+agency.name)

        # else:
        #     print("not found."+pf)

    except Exception as e:
        logger.info(e)
        print(e)
    finally:
        print('finally...')
        logger.info("End")
