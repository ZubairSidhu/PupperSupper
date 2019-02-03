from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from . import mainLogic

def index(request):
	# THIS IS VERY BAD CODE, SORRY
	# It should be done using templates, but I have never used django before
	template = loader.get_template("static/index.html")
	return HttpResponse(template.render())

def about(request):
	template = loader.get_template("static/about.html")
	return HttpResponse(template.render())

@csrf_exempt
def getGoogleCloud(request):
	print(request)
	if request.method == 'POST':
		photoURL = request.POST.get('photo')
		#photoURL = photoURL[21:]
		# print(photoURL)
		print(mainLogic.main(photoURL))
		return HttpResponse('Post')
	else:
		return HttpResponse('Not Post')