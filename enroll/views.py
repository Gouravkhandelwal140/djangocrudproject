from django.shortcuts import render, HttpResponseRedirect, redirect

from .form import Student
from .models import User


# Create your views here.
def addshow(request):
    if (request.method == 'POST'):
        fm = Student(request.POST)
        if (fm.is_valid()):
            nm = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            md = User(name=nm, email=email, password=password)
            md.save()
            return redirect('addshow')
    else:
        fm = Student()
    stud = User.objects.all()
    return render(request, 'enroll/addshow.html', {'form': fm, 'stud': stud})


def update(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = Student(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi = User.objects.get(pk=id)
        fm = Student(instance=pi)
    return render(request, 'enroll/update.html', {'fm': fm})


def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
