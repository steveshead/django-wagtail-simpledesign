from django.views import generic

class TemplatePage(generic.TemplateView):
    template_name = "template.html"

class ServicesPage(generic.TemplateView):
    template_name = "services.html"
