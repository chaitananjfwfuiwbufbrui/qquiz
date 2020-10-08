from django.contrib import admin

# Register your models here.
from home.models import *
admin.site.register(Topics)
admin.site.register(Quuestions)

admin.site.register(users)
admin.site.register(no_tests)