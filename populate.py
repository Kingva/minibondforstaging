import os
import uuid

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'react.settings')

import django

django.setup()

from miniBond.models import *


def populate():
	platform = add_platform('Python', "http://djangobook.py3k.cn/2.0/chapter02/")


	# Print out what we have added to the user.
	# for c in Category.objects.all():
	#     for p in Page.objects.filter(category=c):
	#         print "- {0} - {1}".format(str(c), str(p))


def add_platform(name, website):
	p = Platform(id=uuid.uuid1(), name=name, website= website)
	p.save()


# Start execution here!
if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()
