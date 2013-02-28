from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Addresses

def main(request):
    return render_to_response('main.html', {'addresses':[]},
                              context_instance=RequestContext(request))
