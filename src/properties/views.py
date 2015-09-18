from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from models import Property, Graph
from django.db.models import Q

import re


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
                zipcodes = re.findall(r'\d{4}', query)
                zipcodes_search = None
                if zipcodes:
                    for code in zipcodes:
                        if zipcodes_search:
                            zipcodes_search = zipcodes_search | Q(address2__startswith=code)
                        else:
                            zipcodes_search = Q(address2__startswith=code)
                        query.replace(code, '')
                text_search = None
                text_query = ''.join(i for i in query if not i.isdigit())
                if text_query:
                    for word in text_query.split():
                        word = str(word).strip()
                        if word:
                            if text_search:
                                text_search = text_search | Q(address1__icontains=word) | Q(address2__icontains=word)
                            else:
                                text_search = Q(address1__icontains=word) | Q(address2__icontains=word)
                if zipcodes_search:
                    if text_search:
                        results = Property.objects.filter(zipcodes_search | text_search)
                    else:
                        results = Property.objects.filter(zipcodes_search)
                else:
                    if text_search:
                        print text_search, text_query
                        results = Property.objects.filter(text_search)
                    else:
                        results = Property.objects.all()
        else:
            results = []
        paginator = Paginator(results, 20)  # Show 10 results per page
        results = {"results": paginator.page(page),
                   "method": "simple",
                   "total": paginator.count}
        for key, val in request.GET.iteritems():
            results[key] = str(val)
        return render_to_response('search.html',
                                  RequestContext(request, results))
    return redirect('home')


@login_required()
def property(request, id):
    prop = Property.objects.get(pk=id)
    graphs = Graph.objects.filter(property=id)
    return render_to_response('property.html',
                              RequestContext(request, {'property': prop,
                                                       'graphs': graphs
                                                       }))


@login_required()
def advanced_search(request):
    if request.method == 'GET':
        year = request.GET.get('year', None)
        floor = request.GET.get('floor', None)
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
        if rooms != '' and rooms is not None:
            params['rooms'] = rooms
        if town != '' and town is not None:
            params['address2__icontains'] = town
        if street != '' and street is not None:
            params['address1__icontains'] = street
        if zipcode != '' and zipcode is not None:
            params['address2__startswith'] = zipcode
        results = Property.objects.filter(**params)
        paginator = Paginator(results, 20)  # Show 10 results per page
        results = {"results": paginator.page(page),
                   "method": "advanced",
                   "total": paginator.count}
        for key, val in request.GET.iteritems():
            results[key] = str(val)
        return render_to_response('advanced_search.html',
                                  RequestContext(request, results))
    return redirect('home')
