from django.shortcuts import render, redirect, render, get_object_or_404
from .models import Room, ComponentImage
from .forms import RoomForm, ImageForm


def indexView(request):

    if request.method == "POST":
        form = RoomForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RoomForm()

    rooms = Room.objects.all()
    components = ComponentImage.objects.all()


    template_dir = 'panorama/index.html'
    context = {
        'form': form,
        'rooms': rooms,
        'components': components,
    }

    return render(request, template_dir, context)

def addComponent(request, pk):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES or None)
        if form.is_valid():
            comp = form.save(commit=False)
            comp.room = get_object_or_404(Room, id=pk)
            comp.save()
            return redirect('/')
    else:
        form = ImageForm()
    template_dir = 'panorama/component.htm'
    context = {
        'form': form,
    }

    return render(request, template_dir, context)