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
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    # 'django.contrib.staticfiles',
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


if __name__ == "__main__":
    try:
        agency = PromotionAgency.objects.filter(name="返利魔方").first()
        promotions = PromotionInfo.objects.filter(promotionAgency=agency)
        promotions.delete()

        for pageindex in range(1, 6):
            # print(pageindex)

            # values = {"currentPage": pageindex}
            values = {"page": pageindex}
            data = urllib.parse.urlencode(values).encode(encoding='UTF8')
            hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                   'Accept-Encoding': 'none',
                   'Accept-Language': 'en-US,en;q=0.8',
                   'Connection': 'keep-alive'}

            url = "http://www.fanlimofang.com/activity"
            request = urllib.request.Request(url, data, headers=hdr)
            response = urllib.request.urlopen(request)
            html = response.read().decode('utf-8')
            # print(html)

            pattern = re.compile(
                '<a href="/Activity/Detail/(.*?)">.*?<div class="bonus">(.*?)</div>.*?<div class="keyword">(.*?)</div>.*?</a>', re.S | re.I)
            items = re.findall(pattern, html)
            for item in items:
                # print(item)

                link = "http://www.fanlimofang.com/Activity/Detail/"+item[0]
                print(link)
                dr = re.compile(r'<[^>]+>', re.S)
                bonus = dr.sub('', item[1]).strip().replace(
                    "\n", "").replace("\r", "")
                print(''.join(bonus.split(" ")))
                pfname = re.findall("<span>(.*?)</span>", item[2])[1]

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
                    print(platform.name+"+++"+agency.name)

                else:
                    print("not found."+pfname)

    except e:
        # logger.info(e)
        print(e)
    finally:
        print('finally...')
        # logger.info("End")
