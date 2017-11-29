from django.shortcuts import render
from django.conf import settings as django_settings
from web.utils import getGlobalContext
from web.views import indexExtraContext

def index(request):
    context = getGlobalContext(request)
    indexExtraContext(context)
    context['left_character'] = django_settings.HOMEPAGE_CHARACTERS[0]
    context['right_character'] = django_settings.HOMEPAGE_CHARACTERS[1]
    return render(request, 'pages/indexBackground.html', context)
