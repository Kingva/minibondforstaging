# # from WindPy import w
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


def writeData(date, type, itemstrs):
    olderInter = Interests.objects.filter(date=day, type=type)
    if olderInter:
        olderInter.delete()
    re = w.edb(itemstrs, day.strftime('%Y-%m-%d'),
               day.strftime('%Y-%m-%d'), "Fill=Previous")
    oneInter = Interests(date=day, type=type)
    oneInter.calDeri(re.Data[0])
    oneInter.save()

    print(date.strftime('%Y-%m-%d') + "-" + type + "interest fetch and saved")
    logger.info(date.strftime('%Y-%m-%d') + "-" +
                type + "interest fetch and saved")

if __name__ == "__main__":

    try:
        data = datasettoimport()
        org = RatingOrganization.objects.filter(
            name=data.ratingorganization).first()
        org = org if org else RatingOrganization()
        org.name = data.ratingorganization
        org.save()

        orgRated = PlatformRating.objects.filter(ratingOrganization=org)
        orgRated.delete()

        for rateitem in (data.rating):
            platform = Platform.objects.filter(name=rateitem[0]).first()
            platform = platform if platform else Platform()
            platform.name = rateitem[0]
            platform.save()
            print(rateitem)

            pfRating = PlatformRating(platForm=platform, ratingOrganization=org, url=rateitem[
                                      2], ratingValue=rateitem[1])
            pfRating.save()

            logging.info(org.name+"+++"+platform.name+"+++"+str(rateitem[1]))

            print(org.name+"+++"+platform.name+"+++"+str(rateitem[1]))

    except e:
        logger.info(e)
        print(e)
    finally:
        print('finally...')
        logger.info("End")
