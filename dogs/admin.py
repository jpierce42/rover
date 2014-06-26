from django.contrib import admin
from dogs.models import Owner, Dog


class DogInline(admin.StackedInline):
    model = Dog
    extra = 1


class OwnerAdmin(admin.ModelAdmin):
    inlines = [DogInline]


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Dog)
