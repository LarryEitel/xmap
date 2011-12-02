from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home/base.html"