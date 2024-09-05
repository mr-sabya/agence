from django.shortcuts import render

from website.models import Banner, ServiceSection, Service, AboutSection, GoalSection, PortfolioSection, TestimonialSection
from portfolio.models import TeamMember, Portfolio, Testimonial
from blog.models import Post


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
    
    
    #portfolio section
    try:
        portfolio_section = PortfolioSection.objects.latest('id')
    except:
        portfolio_section = ''
        
    
    #testimonial section
    try:
        testimonial_section = TestimonialSection.objects.latest('id')
    except:
        testimonial_section = ''
    
    services = Service.objects.order_by('id')[:4]
    teams = TeamMember.objects.order_by('id')[:4]
    projects = Portfolio.objects.order_by('id')[:6]
    testimonials = Testimonial.objects.order_by('id')[:3]
    posts = Post.objects.order_by('id')[:3]

    context = {
        'title': 'Home',
        'banner': banner,
        'service_section': service_section,
        'services': services,
        'about_section': about_section,
        'goal_section': goal_section,
        'portfolio_section': portfolio_section,
        'projects': projects,
        'teams': teams,
        'testimonials': testimonials,
        'testimonial_section': testimonial_section,
        'posts': posts
    }
    return render(request, 'home/index.html', context)
