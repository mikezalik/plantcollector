from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plant
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
    care_form = CareForm
    return render(request, 'plants/detail.html', {'plant': plant, 'care_form': care_form})

class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'

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