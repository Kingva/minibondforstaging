# # from WindPy import w
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


def writeData(urllabel, organizationname):
    values = {"currentPage": 0}
    data = urllib.parse.urlencode(values).encode(encoding='UTF8')
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

    url = "http://www.dailuopan.com/pingji/"+urllabel
    request = urllib.request.Request(url, data, headers=hdr)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    # print(html)
    org = RatingOrganization.objects.filter(
        name=organizationname).first()
    org = org if org else RatingOrganization()
    org.name = organizationname
    org.save()
    orgRated = PlatformRating.objects.filter(ratingOrganization=org)
    orgRated.delete()

    pattern = re.compile(
        '<td class="t1.*?>(.*?)</td>.*?target="_blank">(.*?)</a>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        sortindex = item[0]
        pfname = item[1]

        dr = re.compile(r'<[^>]+>', re.S)
        pfname = dr.sub('', pfname).strip().replace(
            "\n", "").replace("\r", "")

        platform = Platform.objects.filter(name=pfname).first()
        platform = platform if platform else Platform()
        platform.name = pfname
        platform.save()
        print(pfname)

        pfRating = PlatformRating(
            platForm=platform, ratingOrganization=org, url="", ratingValue=sortindex)
        pfRating.save()

        logging.info(org.name+"+++"+platform.name+"+++"+str(sortindex))

        print(org.name+"+++"+platform.name+"+++"+sortindex)


if __name__ == "__main__":

    try:
        urllabels = ["wdzj", "p2peye", "rong360"]
        organizationnames = ["网贷之家", "网贷天眼", "融360"]
        for index, org in enumerate(organizationnames):
            writeData(urllabels[index], org)

        # data = datasettoimport()

        # for rateitem in (data.rating):

    except e:
        logger.info(e)
        print(e)
    finally:
        print('finally...')
        logger.info("End")
