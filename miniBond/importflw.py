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


if __name__ == "__main__":

    try:
        pf = "e周行"
        url = "http://shop.fanli.com/home/licai/detail?id=1601&spm=licai_home.pc.pty-go~ptid-2076~std-28996"
        comments = "首次投资最高返利：180元+投资金额x1%"
        isvalid = 1

        platform = Platform.objects.filter(name=pf).first()
        agency = PromotionAgency.objects.filter(name="返利网").first()
        if platform and agency:
            promotion = PromotionInfo.objects.filter(
                platForm=platform, promotionAgency=agency).first()
            promotion = promotion if promotion else PromotionInfo()
            promotion.url = url
            promotion.description = comments
            promotion.platForm = platform
            promotion.promotionAgency = agency
            promotion.isValid = isvalid
            promotion.save()
            platform.isValid = platform.isValid if not isvalid else isvalid
            platform.save()
            print(platform.name+"+++"+agency.name)

        else:
            print("not found."+pf)

    except e:
        logger.info(e)
        print(e)
    finally:
        print('finally...')
        logger.info("End")
