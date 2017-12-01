from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from miniBond.models import *
from django.template.loader import render_to_string
import os
import uuid
from datetime import datetime


def hello(request):
    message = 'hello'
    return HttpResponse("Hello world")


def myname(request, offset):
    name = "wqfaa"
    return render(request, 'miniBond/sample.html', locals())


def index(request):
    # allpfs = Platform.objects.filter(isValid=True)
    # pfs = [p for p in allpfs if p.promotioninfo_set.filter(
    #     isValid=True).count() > 0 or (hasattr(p, 'linktowx') and p.linktowx.isValid)]
    # contextDict = {'pfs': pfs}
    templateName = "index.html"
    # staticView(contextDict, templateName, templateName)
    response = render(request, "static/"+templateName)
    if "cookieId" not in request.COOKIES:
        response.set_cookie("cookieId", uuid.uuid4())
    return response


def staticView(contextDict, templateName, staticFileName):
    static_html = 'templates/static/' + staticFileName
    if not os.path.exists(static_html):
        content = render_to_string('miniBond/' + templateName, contextDict)
        with open(static_html, 'w', encoding="utf-8") as static_file:
            static_file.write(content)


def logTrace(request, areaType, target, propertyData):
    trace = ClickTrace()
    trace.areaType = areaType
    trace.target = target
    trace.propertyData = propertyData
    trace.clickTime = datetime.now()
    cookieId = request.COOKIES[
        "cookieId"] if "cookieId" in request.COOKIES else uuid.uuid4()
    trace.cookieId = cookieId
    trace.save()

    response = HttpResponse('')
    if "cookieId" not in request.COOKIES:
        response.set_cookie("cookieId", cookieId)
    return response


def toWx(request, uuid):
    staticFileName = str(uuid)+".html"
    return render(request, "static/" + staticFileName)


def strongStaticView(contextDict, templateName, staticFileName):
    static_html = 'templates/static/' + staticFileName
    content = render_to_string('miniBond/' + templateName, contextDict)
    with open(static_html, 'w', encoding="utf-8") as static_file:
        static_file.write(content)


def refreshCache(request):
    allpfs = Platform.objects.all()
    pfs = [p for p in allpfs if
           (hasattr(p, 'linktowx') and p.linktowx.isValid)]

    contextDict = {'pfs': pfs}
    templateName = "index.html"
    strongStaticView(contextDict, templateName, templateName)

    allpfs = Platform.objects.all()
    for pf in allpfs:
        if hasattr(pf, 'linktowx'):
            toWxItem = LinkToWx.objects.filter(platForm__id=pf.id).first()
            contextDict = {'wxText': toWxItem.wxText,
                           'imgName': toWxItem.image, 'pfName': toWxItem.platForm.name}

            staticFileName = str(toWxItem.platForm.id) + ".html"
            strongStaticView(contextDict, "linkToWx.html", staticFileName)

    response = HttpResponse('well done!')
    return response
