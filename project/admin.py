from django.contrib import admin
from project.models import Project,Pledger,ProjectUpdates
# Register your models here.
admin.site.register(Project)
admin.site.register(Pledger)
admin.site.register(ProjectUpdates)