from django.shortcuts import render
import hashlib
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
@csrf_exempt
def erduo(request):
	if request.method == "GET":
		signature = request.GET.get('signature',None)
		timestamp = request.GET.get('timestamp',None)
		nonce = request.GET.get('nonce',None)
		echostr = request.GET.get('echostr',None)
		token = 'nx5bw'

		hashlist = [token,timestamp,nonce]
		hashlist.sort()
		hashstr = hashlib.sha1(hashstr).hexdigest()
		if hashstr == signature:
			return HttpResponse(echostr)
		else:
			return HttpResponse("field")

	else:
		othercontent =autoreply(request)
		return HttpResponse(othercontent)
def autoreply(request):
	pass

	