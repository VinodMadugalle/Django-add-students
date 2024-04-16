from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import postTable
from django.template import loader
from .forms import createPost

def studentapp(request):
    database=postTable.objects.all()
    return render(request,'home.html', {'database':database})

def createNewPost(request):
    form=createPost()
    if request.method == "POST":
        form = createPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentapp')

    return render(request,('form.html'),{'form':form})

def updatePost(request,pid):
    database = postTable.objects.get(id=pid)
    form = createPost(instance=database)
    if request.method == "POST":
        form = createPost(request.POST, instance=database)
        if form.is_valid():
            form.save()
            return redirect('studentapp')
    return render(request, 'form.html', {'form':form})

def delete(request,pid):
    database= postTable.objects.get(id=pid)
    if request.method == "POST":
        database.delete()
        return redirect('studentapp')
    return render(request, 'del.html')

def view(request,pid):
    database= postTable.objects.get(id=pid)
    return render(request,'view.html',{'database':database})