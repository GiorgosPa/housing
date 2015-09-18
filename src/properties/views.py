from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required


@login_required()
def search(request):
	 return render_to_response('search.html',
                               RequestContext(request))