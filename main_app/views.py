from typing import List
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import os
import boto3
import uuid
from .models import Plant, Photo
from .forms import CareForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# View functions

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def plants_index(request):
    plants = Plant.objects.filter(user=request.user)
    return render(request, 'plants/index.html', {
        'plants': plants,
    })

@login_required
def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    care_form = CareForm()
    return render(request, 'plants/detail.html', {'plant': plant, 'care_form': care_form})

class PlantCreate(LoginRequiredMixin, CreateView):
    model = Plant
    fields = ['name', 'species', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlantUpdate(LoginRequiredMixin, UpdateView):
    model = Plant
    fields = ['name', 'species', 'description']

class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = '/plants/'

@login_required
def add_care(request, plant_id):
    form = CareForm(request.POST)

    if form.is_valid():
        new_care = form.save(commit=False)
        new_care.plant_id = plant_id
        new_care.save()
    return redirect('detail', plant_id = plant_id)

@login_required
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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid Sign Up - Try Again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)