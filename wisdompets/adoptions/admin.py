from django.contrib import admin

from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):

    # This list is defined in django, but we "override" it so that it displays the specific
    # attributes we want it to display from the Pet model.
    list_display = ['name', 'species', 'breed', 'age', 'sex']
