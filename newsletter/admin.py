from django.contrib import admin
from .models import SignUp
# Register your models here.
from .forms import SingUpForm

class SingUpAdmin(admin.ModelAdmin):
    list_display = ('__str__','timestamp','updated')
    form = SingUpForm
    # class Meta:
    #     model = SignUp
admin.site.register(SignUp,SingUpAdmin)