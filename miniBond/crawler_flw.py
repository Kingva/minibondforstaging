# # from WindPy import w
import os
import sys
import re

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
        192.168.20.75
        # :27017
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
        # http://shop.fanli.com/Home/licai/ajaxGetUserShops?userid=185331149&t=1514966380691
        # json = u'{"info":"ok","data":{"shopList":[{"shop_name":"e\u5468\u884c","shop_logo":"http:\/\/l0.51fanli.net\/shop\/images\/2017\/10\/59e6ca597013b.jpg","profit":"7.9~12.5","fanli_desc":"220<\/em>\u5143+<\/i>\u6295\u8d44\u91d1\u989dx<\/i>1<\/em>%<\/small>","link":"http:\/\/shop.fanli.com\/home\/licai\/detail?id=1919","shop_state":"2","buy_state":0,"shop_id":"2076","end_time":"1521647999","end_day":3},{"shop_name":"\u5b9c\u4eba\u8d22\u5bcc","shop_logo":"http:\/\/l0.51fanli.net\/shop\/images\/2017\/11\/5a044e48c4dfb.jpg","profit":"5~9.9","fanli_desc":"150<\/em>\u5143+<\/i>\u6295\u8d44\u91d1\u989dx<\/i>1<\/em>%<\/small>","link":"http:\/\/shop.fanli.com\/home\/licai\/detail?id=1917","shop_state":"2","buy_state":0,"shop_id":"2057","end_time":"1521647999","end_day":3},{"shop_name":"\u94b1\u591a\u591a","shop_logo":"http:\/\/l1.51fanli.net\/shop\/images\/2017\/12\/5a2761301f4c3.jpg","profit":"7.2~11.2","fanli_desc":"120<\/em>\u5143+<\/i>\u6295\u8d44\u91d1\u989dx<\/i>1<\/em>%<\/small>","link":"http:\/\/shop.fanli.com\/home\/licai\/detail?id=1927","shop_state":"2","buy_state":0,"shop_id":"2210","end_time":"1521647999","end_day":3},{"shop_name":"\u767e\u91d1\u8d37","shop_logo":"http:\/\/l0.51fanli.net\/shop\/images\/2018\/01\/5a6abe6cd998a.jpg","profit":"9~12","fanli_desc":"150<\/em>\u5143+<\/i>\u6295\u8d44\u91d1\u989dx<\/i>1<\/em>%<\/small>","link":"http:\/\/shop.fanli.com\/home\/licai\/detail?id=1925","shop_state":"2","buy_state":0,"shop_id":"2262","end_time":"1521647999","end_day":3},{"shop_name":"\u4eca\u91d1\u8d37","shop_logo":"http:\/\/l0.51fanli.net\/shop\/images\/2017\/11\/5a027e61a8211.jpg","profit":"8.8~16.8","fanli_desc":"150<\/em>\u5143+<\/i>\u6295\u8d44\u91d1\u989dx<\/i>1<\/em>%<\/small>","link":"http:\/\/shop.fanli.com\/home\/licai\/detail?id=1921","shop_state":"2","buy_state":0,"shop_id":"2077","end_time":"1521647999","end_day":3},{"shop_name":"\u6447\u8d22\u6811","shop_logo":"http:\/\/l0.51fanli.net\/shop\/images\/2017\/11\/5a0280315bdf3.jpg","profit":"8~12","fanli_desc":"200<\/em>\u5143+<\/i>\u6295\u8d44\u91d1\u989dx<\/i>1<\/em>%<\/small>","link":"http:\/\/shop.fanli.com\/home\/licai\/detail?id=1923","shop_state":"2","buy_state":0,"shop_id":"2130","end_time":"1521647999","end_day":3},{"shop_name":"\u4f60\u6211\u8d37","shop_logo":"http:\/\/l0.51fanli.net\/shop\/images\/2017\/10\/59e9da318b392.jpg","profit":"5~15","fanli_desc":"100<\/em>\u5143+<\/i>\u6295\u8d44\u91d1\u989dx<\/i>1<\/em>%<\/small>","link":"http:\/\/shop.fanli.com\/home\/licai\/detail?id=1929","shop_state":"2","buy_state":0,"shop_id":"1677","end_time":"1521647999","end_day":3},{"shop_name":"\u56e2\u8d37\u7f51","shop_logo":"http:\/\/l0.51fanli.net\/shop\/images\/2017\/10\/59e9dc17e0126.jpg","profit":"7~12.6","fanli_desc":"200<\/em>\u5143+<\/i>\u6295\u8d44\u91d1\u989dx<\/i>1<\/em>%<\/small>","link":"http:\/\/shop.fanli.com\/home\/licai\/detail?id=1931","shop_state":"2","buy_state":0,"shop_id":"1892","end_time":"1521647999","end_day":3}],"hotList":[],"total_fanli":0},"status":1}'
        json = u'{"info":"ok","data":{"shopList":[{"shop_name":"\u4f60\u6211\u8d37","shop_logo":"http:\/\/l0.51fanli.net\/shop\/images\/2017\/10\/59e9da318b392.jpg","profit":"5~15","fanli_desc":"128<\/em>\u5143+<\/i>\u6295\u8d44\u91d1\u989dx<\/i>1.2<\/em>%<\/small>","link":"\/\/shop.fanli.com\/home\/licai\/detail?id=2085","shop_state":"2","buy_state":0,"shop_id":"1677","end_time":"1525103999","end_day":4},{"shop_name":"\u94b1\u76c6\u7f51","shop_logo":"http:\/\/l2.51fanli.net\/shop\/images\/2018\/04\/5ad4712b6e8b7.jpg","profit":"10~15","fanli_desc":"160<\/em>\u5143+<\/i>\u6295\u8d44\u91d1\u989dx<\/i>1<\/em>%<\/small>","link":"\/\/shop.fanli.com\/home\/licai\/detail?id=2079","shop_state":"2","buy_state":0,"shop_id":"2284","end_time":"1524844799","end_day":0},{"shop_name":"E\u90fd\u5e02\u94b1\u5305","shop_logo":"http:\/\/l0.51fanli.net\/shop\/images\/2018\/03\/5ab4974abcccb.jpg","profit":"7.5~12","fanli_desc":"200<\/em>\u5143+<\/i>\u6295\u8d44\u91d1\u989dx<\/i>1<\/em>%<\/small>","link":"\/\/shop.fanli.com\/home\/licai\/detail?id=2073","shop_state":"2","buy_state":0,"shop_id":"2278","end_time":"1525103999","end_day":4},{"shop_name":"PPmoney","shop_logo":"http:\/\/l1.51fanli.net\/shop\/images\/2018\/04\/5ad483873661c.jpg","profit":"6.5~10","fanli_desc":"200<\/em>\u5143+<\/i>\u6295\u8d44\u91d1\u989dx<\/i>1<\/em>%<\/small>","link":"\/\/shop.fanli.com\/home\/licai\/detail?id=2081","shop_state":"2","buy_state":0,"shop_id":"1908","end_time":"1525103999","end_day":4},{"shop_name":"\u56e2\u8d37\u7f51","shop_logo":"http:\/\/l0.51fanli.net\/shop\/images\/2017\/10\/59e9dc17e0126.jpg","profit":"7~12.6","fanli_desc":"200<\/em>\u5143+<\/i>\u6295\u8d44\u91d1\u989dx<\/i>1<\/em>%<\/small>","link":"\/\/shop.fanli.com\/home\/licai\/detail?id=2071","shop_state":"2","buy_state":0,"shop_id":"1892","end_time":"1525103999","end_day":4},{"shop_name":"\u6447\u8d22\u6811","shop_logo":"http:\/\/l0.51fanli.net\/shop\/images\/2017\/11\/5a0280315bdf3.jpg","profit":"8~12","fanli_desc":"200<\/em>\u5143+<\/i>\u6295\u8d44\u91d1\u989dx<\/i>1<\/em>%<\/small>","link":"\/\/shop.fanli.com\/home\/licai\/detail?id=2077","shop_state":"2","buy_state":0,"shop_id":"2130","end_time":"1525103999","end_day":4},{"shop_name":"\u94b1\u591a\u591a","shop_logo":"http:\/\/l1.51fanli.net\/shop\/images\/2017\/12\/5a2761301f4c3.jpg","profit":"7.2~11.2","fanli_desc":"120<\/em>\u5143+<\/i>\u6295\u8d44\u91d1\u989dx<\/i>1<\/em>%<\/small>","link":"\/\/shop.fanli.com\/home\/licai\/detail?id=2075","shop_state":"2","buy_state":0,"shop_id":"2210","end_time":"1525103999","end_day":4}],"hotList":[{"id":"10163","shop_name":"\u94b1\u76c6\u7f51","shop_id":"2284","hot_goods_logo":"http:\/\/l1.51fanli.net\/shop\/images\/2018\/04\/5adf545e899f8.png","name":"\u975e\u65b0\u624b1\u6708\u6807","link":"\/\/shop.fanli.com\/Home\/licai\/detail?id=2079","fanli_rule":"\u8fd4\u5229:50<\/em>\u5143+<\/i>\u6295\u8d44\u91d1\u989dx<\/i>1<\/em>%<\/small>","profit":"10","desc":"\u6210\u7acb\u4e8e2012\u5e7410\u670817\u65e5\uff0c\u5df2\u4e0e\u65b0\u7f51\u94f6\u884c\u7b7e\u8ba2\u94f6\u884c\u5b58\u7ba1\u534f\u8bae","end_day":0,"end_time":"1524844799"}],"total_fanli":0},"status":1}'

        isvalid = 1
        agency = PromotionAgency.objects.filter(name="返利网").first()
        promotions = PromotionInfo.objects.filter(promotionAgency=agency)
        promotions.delete()

        pattern = re.compile(
            '"shop_name":"(.*?)".*?"fanli_desc":"(.*?)".*?"link":"(.*?)",', re.S)
        items = re.findall(pattern, json)
        for item in items:
            pfname = "宜人贷" if item[0] == "宜人财富" else item[0]
            # print(pfname)
            link = item[2]
            # print(link)
            bonus = "首次投资最高返利：" + item[1]
            dr = re.compile(r'<[^>]+>', re.S)
            bonus = dr.sub('', bonus).strip().replace(
                "\n", "").replace("\r", "")
            # print(''.join(bonus.split(" ")))

            platform = Platform.objects.filter(name=pfname).first()

            if platform:
                promotion = PromotionInfo()
                promotion.url = link
                promotion.description = bonus
                promotion.platForm = platform
                promotion.promotionAgency = agency
                promotion.isValid = isvalid
                promotion.save()
                platform.isValid = platform.isValid if not isvalid else isvalid
                platform.save()
                print(platform.name + "+++" + agency.name)

            else:
                print("not found." + pfname)

        # isvalid = 1

        # agency = PromotionAgency.objects.filter(name="返利网").first()
        # promotions = PromotionInfo.objects.filter(promotionAgency=agency)
        # promotions.delete()

        # pfs = ["钱多多", "知商金融", ]
        # ids = [1679, 1669, ]
        # messages = ["120元+投资金额x1%", "160元+投资金额x1%", ]

        # for index, pf in enumerate(pfs):
        #     # print(pf)
        #     url = "http://shop.fanli.com/home/licai/detail?id="+str(ids[index])
        #     # print(url)
        #     message = "首次投资最高返利："+messages[index]
        #     # print(message)

        #     platform = Platform.objects.filter(name=pf).first()

        #     if platform:
        #         promotion = PromotionInfo()
        #         promotion.url = url
        #         promotion.description = message
        #         promotion.platForm = platform
        #         promotion.promotionAgency = agency
        #         promotion.isValid = isvalid
        #         promotion.save()
        #         platform.isValid = platform.isValid if not isvalid else isvalid
        #         platform.save()
        #         print(platform.name+"+++"+agency.name)

        #     else:
        #         print("not found."+pf)

    except e:
        logger.info(e)
        print(e)
    finally:
        print('finally...')
        logger.info("End")
