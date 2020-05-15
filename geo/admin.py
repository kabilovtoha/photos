from django.contrib import admin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)

from .models import City, Photo

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ('name', )




def photo_make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)

def photo_unpublishe(modeladmin, request, queryset):
    queryset.update(is_published=False)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_filter = (
        'is_published',
        ('city', RelatedDropdownFilter),
    )
    # fields = ('id', 'ident', 'key', 'val', 'vals_array')
    list_display = ('author', 'id', 'city', 'image', 'is_published')
    actions = [photo_make_published, photo_unpublishe]
