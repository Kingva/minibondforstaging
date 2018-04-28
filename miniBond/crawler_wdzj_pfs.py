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

        for pageindex in range(1, 2):
            print(pageindex)

            values = {"currentPage": pageindex}
            data = urllib.parse.urlencode(values).encode(encoding='UTF8')
            hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                   'Accept-Encoding': 'none',
                   'Accept-Language': 'en-US,en;q=0.8',
                   'Connection': 'keep-alive'}

            url = "http://www.wdzj.com/dangan/search?filter=e1"
            request = urllib.request.Request(url, data, headers=hdr)
            response = urllib.request.urlopen(request)
            html = response.read().decode('utf-8')

            pattern = re.compile(
                '<li class="item">.*?<a href="(.*?)" target="_blank">(.*?)</a>(.*?)<div class="itemCon clearfix">', re.S)
            items = re.findall(pattern, html)
            for item in items:
                print(item[0])
                print(item[1])
                emitems = re.findall("<em>(.*?)</em>", item[2])
                labeldesc = ""
                for emitem in emitems:
                    if emitem.find("评级") < 0:
                        labeldesc = emitem+" "+labeldesc

                labeldesc = " + ".join(labeldesc.strip(" ").split(" "))
                print(labeldesc)

                platform = Platform.objects.filter(name=item[1]).first()
                platform = platform if platform else Platform()
                platform.name = item[1]
                platform.website = "http://www.wdzj.com"+item[0]
                platform.comments = labeldesc
                platform.save()

    except e:
        # logger.info(e)
        print(e)
    finally:
        print('finally...')
        # logger.info("End")
