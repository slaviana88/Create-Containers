from django.shortcuts import render, redirect
from .forms import ContainerForm
from .models import Container


def index(request):
    containers = Container.objects.all()
    return render(request, "index.html", locals())


def create_container(request):
    if request.method == 'POST':
        form = ContainerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContainerForm()

    return render(request, "start.html", locals())
