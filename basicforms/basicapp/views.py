from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'basicapp/index.html')


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Validation Success!")
            print(form.cleaned_data['name'])

    return render(request, 'basicapp/form.html', {'form': form})


def users(request):
    form = forms.NewUserForm()
    if request.method == "POST":
        form = forms.NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID!')

    return render(request, 'basicapp/users.html', {'form': form})
