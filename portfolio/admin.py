from django.contrib import admin
from .models import Project
from .models import Certificate
from .models import InformationAboutMe

admin.site.register(Project)
admin.site.register(Certificate)
admin.site.register(InformationAboutMe)
