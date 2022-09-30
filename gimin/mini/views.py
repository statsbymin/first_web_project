from django.views.generic import *

class HomeView(TemplateView):
    template_name = 'index.html'
    
class AboutView(TemplateView):
    template_name = 'about.html'
    
class ResumeView(TemplateView):
    template_name = 'resume.html'
    
class ServicesView(TemplateView):
    template_name = 'services.html'
    
class PortfolioView(TemplateView):
    template_name = 'portfolio.html'
    
class PortfoliodetailsView(TemplateView):
    template_name = 'portfolio-details.html'
