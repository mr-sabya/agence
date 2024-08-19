from django.shortcuts import render

from website.models import Banner, ServiceSection, Service


def index(request):
    
    
    try:
        banner = Banner.objects.latest('id')
    except:
        banner = ''
        
    try:
        service_section = ServiceSection.objects.latest('id')
    except:
        service_section = ''
    
    services = Service.objects.order_by('id')

    context = {
        'title': 'Home',
        'banner': banner,
        'service_section': service_section,
        'services': services,
    }
    return render(request, 'home/index.html', context)
