from django.shortcuts import render, redirect
from HOW.forms import AssistForm
from HOW.models import Assist


def home(request):
    data = {}
    data['db'] = Assist.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = AssistForm()
    return render(request, 'form.html', data)


def create(request):
    form = AssistForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Assist.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Assist.objects.get(pk=pk)
    data['form'] = AssistForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Assist.objects.get(pk=pk)
    form = AssistForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Assist.objects.get(pk=pk)
    db.delete()
    return redirect('home')