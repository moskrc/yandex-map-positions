from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from forms import PositionForm
from models import Position


def index(request):
    positions = Position.objects.all()
    return render(request, 'example/index.html', {'positions': positions})


def add(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = PositionForm()

    return render(request, 'example/add.html', {'form': form})


def edit(request, position_id):

    position = get_object_or_404(Position, pk=position_id)

    if request.method == 'POST':
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
    else:
        form = PositionForm(instance=position)

    return render(request, 'example/edit.html', {'form': form})
