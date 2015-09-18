from django.template import RequestContext
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Property


@login_required()
def search(request):
    if request.method == 'GET':
        query = request.GET.get('query', None)
        page = request.GET.get('page', '1')
        try:
            page = int(page)
        except ValueError:
            page = 1
        if query is not None:
            if query == '':
                results = Property.objects.all()
            else:
                results = Property.objects.filter(address1__contains=query)             
        else:
            results = []        
        paginator = Paginator(results, 10) # Show 10 results per page
        results = {"results": paginator.page(page),
                   "method": "simple"}
        for key, val in request.GET.iteritems():
            results[key] = str(val)
        return render_to_response('search.html',
                                  RequestContext(request, results))
    return redirect('home')


@login_required()
def advanced_search(request):
    if request.method == 'GET':
        year = request.GET.get('year', None)
        floor = request.GET.get('floor', None)
        floors = request.GET.get('floors', None)
        rooms = request.GET.get('rooms', None)
        street = request.GET.get('street', None)
        zipcode = request.GET.get('zipcode', None)
        town = request.GET.get('town', None)
        page = request.GET.get('page', '1')
        try:
            page = int(page)
        except ValueError:
            page = 1
        if year is None and \
            floor is None and \
            floors is None and \
            rooms is None and \
            street is None and \
            zipcode is None and \
            town is None:
            return render_to_response('advanced_search.html',
                                      RequestContext(request))
        params = {}
        if year != '' and year is not None:
            params['year'] = year
        if floor != '' and floor is not None:
            params['floor'] = floor
        if floors != '' and floors is not None:
            params['floors'] = floors
        if rooms != '' and rooms is not None:
            params['rooms'] = rooms
        if town != '' and town is not None:
            params['address2__contains'] = town
        if street != '' and street is not None:
            params['address1__contains'] = street
        if zipcode != '' and zipcode is not None:
            params['address2__startswith'] = zipcode
        results = Property.objects.filter(**params)
        paginator = Paginator(results, 10) # Show 10 results per page
        results = {"results": paginator.page(page),
                   "method": "advanced"}
        for key, val in request.GET.iteritems():
            results[key] = str(val)
        return render_to_response('advanced_search.html',
                                  RequestContext(request, results))
    return redirect('home')
