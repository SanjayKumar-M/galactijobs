from django.contrib import admin
from .models import *

admin.site.register(Users)
admin.site.register(Candidate)
admin.site.register(Company)
admin.site.register(JobDetail)