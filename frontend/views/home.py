from django.shortcuts import render

from website.models import Banner, ServiceSection, Service, AboutSection, GoalSection


def index(request):
    
    #banner
    try:
        banner = Banner.objects.latest('id')
    except:
        banner = ''
    
    #service section
    try:
        service_section = ServiceSection.objects.latest('id')
    except:
        service_section = ''
        
    #about section
    try:
        about_section = AboutSection.objects.latest('id')
    except:
        about_section = ''
        
    
    #goal section
    try:
        goal_section = GoalSection.objects.latest('id')
    except:
        goal_section = ''
    
    services = Service.objects.order_by('id')

    context = {
        'title': 'Home',
        'banner': banner,
        'service_section': service_section,
        'services': services,
        'about_section': about_section,
        'goal_section': goal_section,
    }
    return render(request, 'home/index.html', context)
