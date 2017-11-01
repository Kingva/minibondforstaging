from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context


def hello(request):
	message = 'hello'
	assert(False)
	return HttpResponse("Hello world")

def myname(request):
	name = "wqfaa"
	return render_to_response('sample.html', locals())