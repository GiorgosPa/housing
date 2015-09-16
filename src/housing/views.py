from django.template.loader import get_template
from django.http import HttpResponse


def home(request):
    template = get_template('home.html')
    html = template.render()
    return HttpResponse(html)
