from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

from models import Addresses

def main(request):
    addresses = Addresses.objects.all()
    errors = []
    if request.method == 'POST':
        required = ['name', 'line_one', 'city', 'state', 'zip_code']
        for entry in required:
            if not request.POST.get(entry, ''):
                errors.append(entry)
        if not errors:
            new_addr = Addresses.objects.create(name=request.POST['name'],
                                 line_one=request.POST['line_one'],
                                 line_two=request.POST['line_two'],
                                 city=request.POST['city'],
                                 state=request.POST['state'],
                                 zip_code=request.POST['zip_code'],
                                 user=User.objects.get(username=request.user))
    return render_to_response('main.html', {'addresses':addresses, 'errors':errors}, context_instance=RequestContext(request))
