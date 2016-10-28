from django.shortcuts import render

from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from searchengine.gse import google_search
#from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
import pdb
@csrf_exempt
def search(request):
    
    my_api_key = "AIzaSyCfXfB3DUeVWwFpFFqIcliJslJ-qfRJtF8"
    my_cse_id = "012714669292352524483:jg2mcvgqwfy"

    
    if request.POST:
	#pdb.set_trace()
	return render_to_response('search.html', {'result': google_search(request.POST['term'],my_api_key,my_cse_id,num=3 )})
	#return HttpResponseRedirect("/")
    else:
	#pdb.set_trace()
	return render_to_response ('search.html')
