from django.shortcuts import render

from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from searchengine.gse import google_search
#from django.utils import simplejson
from searchengine.dcg import getDCG
from django.views.decorators.csrf import csrf_exempt
import pdb
import math
@csrf_exempt
def search(request):
    
    my_api_key = "AIzaSyCfXfB3DUeVWwFpFFqIcliJslJ-qfRJtF8"
    my_cse_id = "012714669292352524483:jg2mcvgqwfy"

    
    if request.POST:
	#pdb.set_trace()
	return render_to_response('search.html', {'result': google_search(request.POST['term'],my_api_key,my_cse_id,num=10 ),'a':request.POST['term']})
	#return HttpResponseRedirect("/")
    else:
	#pdb.set_trace()
	return render_to_response ('search.html')

@csrf_exempt
def searchradio(request):
    
    #import pdb;
    #pdb.set_trace()
    import math
    val1 = request.POST['val1']
    val2 = request.POST['val2']
    val3 = request.POST['val3']
    #DCG=float(val1)+float(val2)+float(val3)


    DCG=(float(val1)+float(val2)/math.log(2)+float(val3)/math.log(3))/(float(3)+float(3)/math.log(2)+float(3)/math.log(3))
    return HttpResponse("Utility: %s" %DCG)
