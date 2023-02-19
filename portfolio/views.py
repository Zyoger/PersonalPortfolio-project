from django.shortcuts import render, get_object_or_404
from .models import Project
from .models import Certificate


def home(request):
    projects = Project.objects.all()[:3]
    return render(request, "portfolio/home.html", {"projects": projects})


def all_projects(request):
    projects = Project.objects.all()
    return render(request, "portfolio/all_projects.html", {"projects": projects})


def about(request):
    certificates = Certificate.objects.all()
    return render(request, "portfolio/about.html", {"certificates": certificates})
