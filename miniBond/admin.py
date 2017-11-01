from django.contrib import admin

from miniBond.models import *

admin.site.register(Platform)
admin.site.register(RatingOrganization)
admin.site.register(PlatformRating)
admin.site.register(PromotionAgency)
admin.site.register(PromotionInfo)
admin.site.register(LinkToWx)

admin.site.register(LabelText)
admin.site.register(PlatformLabel)


# Register your models here.
