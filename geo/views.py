# -*- coding: utf-8 -*-

from django.shortcuts import render  # noqa

from django.views.generic import TemplateView, FormView
from django.http import JsonResponse

from .forms import PhotoForm
from . import models
from . import serializers
from .db_utils import get_data

class IndexView(TemplateView):
    template_name = 'photos/index.html'

class PhotoView(TemplateView):
    template_name = 'photos/photos.html'

class PhotoAddView(FormView):
    template_name = 'photos/add.html'
    form_class = PhotoForm

    def get(self, request, *args, **kwargs):
        context = {}
        if request.user.is_authenticated:
            form = PhotoForm()
            context = {'form': form}
            return render(request, self.template_name, context)
        return render(request, self.template_name, context)



    def post(self, request, *args, **kwargs):
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            D_cleaned = form.cleaned_data
            D_cleaned['author'] = request.user
            self.save_photo(D_cleaned)
            return render(request, self.template_name, {'success': True, 'form': PhotoForm()})
        else:
            return self.form_invalid(form)

    def save_photo(self, valid_data):
        image = valid_data.get('image')
        print(' + image', image)
        city = valid_data.get('city')
        desc = valid_data.get('desc')
        author = valid_data.get('author')
        photo = models.Photo(image=image, city=city, author=author)
        if desc:
            photo.desc = desc
        photo.save()

def get_photos_filterparams(request):
    context = {}
    sql_str = """select COUNT(photo.id) as photo_count, city.name, photo.city_id as id
    from geo_photo as photo
     left join geo_city as city on photo.city_id = city.id
     GROUP BY city_id"""
    data = get_data(sql_str)

    context['cities'] = data
    return JsonResponse(context)
