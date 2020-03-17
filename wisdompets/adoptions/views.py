from django.shortcuts import render, get_object_or_404
from .models import Pet
# from django.http import Http404


def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets': pets})


def pet_detail(request, id):
    # try:
    #     pet = Pet.objects.get(id=id)
    # except Pet.DoseNotExist:
    #     raise Http404('Pet Not Found!')
    pet = get_object_or_404(Pet, pk=id)
    return render(request, 'pet_detail.html', {'pet': pet})
