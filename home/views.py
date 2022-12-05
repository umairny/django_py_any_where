from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from home.models import Headings, Features, SubFeatures
from django.views.generic import ListView

# Create your views here.

# This is a little complex because we need to detect when we are
# running in various configurations


class HomeView(ListView):
    model = Headings
    def get(self, request):
        projects = Headings.objects.all()
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            "project_list": projects
        }
        return render(request, 'home/main.html', context)

class ProjectListView(ListView):
    model = Headings
    template_name = "home/project.html"
    def get(self, request):
        list = Headings.objects.all()
        
        ctx = {"project_list": list}
        return render(request, self.template_name, ctx)