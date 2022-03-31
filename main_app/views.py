from typing import List
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import os
import boto3
import uuid
from .models import Plant, Photo
from .forms import CareForm

# View functions

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {
        'plants': plants,
    })

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    care_form = CareForm()
    return render(request, 'plants/detail.html', {'plant': plant, 'care_form': care_form})

class PlantCreate(CreateView):
    model = Plant
    fields = ['name', 'species', 'description']

class PlantUpdate(UpdateView):
    model = Plant
    fields = ['name', 'species', 'description']

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'

def add_care(request, plant_id):
    form = CareForm(request.POST)

    if form.is_valid():
        new_care = form.save(commit=False)
        new_care.plant_id = plant_id
        new_care.save()
    return redirect('detail', plant_id = plant_id)

def add_photo(request, plant_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, plant_id=plant_id)
        except:
            print('An error occurred uploading your file to S3')
    return redirect('detail', plant_id=plant_id)