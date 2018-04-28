import urllib.request
import re
import os
import sys

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

CONF_LOG = "loggingconfig.config"
logging.config.fileConfig(CONF_LOG)  # 采用配置文件
logger = logging.getLogger("fetchinterests")

# class bondTradinfo:


if __name__ == "__main__":

    try:
        agency = PromotionAgency.objects.filter(name="掌贷天下").first()
        promotions = PromotionInfo.objects.filter(promotionAgency=agency)
        promotions.delete()

        values = {"name": "zhangdai360", "pass": "getList"}
        data = urllib.parse.urlencode(values).encode(encoding='UTF8')
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}

        url = "http://www.zhangdai360.com/backend/Secret/showList"
        request = urllib.request.Request(url, data, headers=hdr)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        # print(html)

        pattern = re.compile(
            '"name":"(.*?)","detail":"(.*?)","bank_deposit.*?height_rate":"(.*?)"', re.S)
        items = re.findall(pattern, html)
        for item in items:
            pfname = item[0]
            link = item[1]
            bonus = "综合年化" + item[2]

            platform = Platform.objects.filter(name=pfname).first()

            if platform and agency:
                promotion = PromotionInfo.objects.filter(
                    platForm=platform, promotionAgency=agency).first()
                promotion = promotion if promotion else PromotionInfo()
                promotion.url = link
                promotion.description = bonus

                promotion.platForm = platform
                promotion.promotionAgency = agency
                promotion.isValid = 1
                promotion.save()
                platform.isValid = 1
                platform.save()
                print(platform.name + "+++" + agency.name)

            else:
                print("not found." + pfname)

        promotions = PromotionInfo.objects.filter(promotionAgency=agency)
        promotions.delete()

    except e:
        logger.info(e)
        print(e)
    finally:
        print('finally...')
        logger.info("End")
