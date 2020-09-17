from django.contrib import admin
from .models import CoffeeMachine, CoffeePod

# Register your models here.
class CoffeeMachineAdmin(admin.ModelAdmin):
    exclude = ('code',)

class CoffeePodAdmin(admin.ModelAdmin):
    exclude = ('code',)


admin.site.register(CoffeeMachine, CoffeeMachineAdmin)
admin.site.register(CoffeePod, CoffeePodAdmin)