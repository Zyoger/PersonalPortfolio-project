from django.shortcuts import render, get_object_or_404
from .models import Project
from .models import Certificate
from .models import InformationAboutMe


def home(request):
    projects = Project.objects.all()[:3]
    return render(request, "portfolio/home.html", {"projects": projects})


def all_projects(request):
    projects = Project.objects.all()
    return render(request, "portfolio/all_projects.html", {"projects": projects})


def about(request):
    certificates = Certificate.objects.all()[1:]
    first_certificate = Certificate.objects.all()[:1]
    infos = InformationAboutMe.objects.all()[:1]
    return render(request, "portfolio/about.html", {"certificates": certificates, "infos": infos, "first_certificate":first_certificate})


def view_project(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    return render(request, "portfolio/project.html", {"project": project})
