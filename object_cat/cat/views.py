from django.http import HttpResponse, Http404, HttpRequest
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Cat, User
from django.db.models import Q
from django.http import HttpResponseRedirect

from .forms import Catform, Userform, totalUserform, editUserform

#gives detail about a cat and his owner
def detail(request, cat_id, user_id):
    cat = get_object_or_404(Cat, pk=cat_id)
    user = get_object_or_404(User, pk=cat.userid_id)
    return render(request, 'cat/detail.html', {'cat': cat, 'user': user, 'userid':user_id})

#gives detail about a user and his cats
def udetail(request, user_id):
    myvide = False
    elsevide = False
    user = get_object_or_404(User, pk=user_id)
    list_of_mycats = Cat.objects.filter(userid=user_id)
    if (len(list_of_mycats)==0):
        myvide= True
    list_of_cats = Cat.objects.filter(~Q(userid =user_id))
    if (len(list_of_cats)==0):
        elsevide=True
    return render(request, 'user/udetail.html', {'user':user, 'list_of_mycats':list_of_mycats, 'list_of_cats': list_of_cats, 'myvide':myvide, 'elsevide':elsevide})

#pages where you can connect to your account
def connection(request):
    already = False #used to show an error message if the user doesn't exist
    form = Userform()
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            result = form.cleaned_data
            if User.objects.filter(email=result['email']).exists():
                user = User.objects.get(email=result['email'])
                if (user.password == result['password']):#check if the password is correct
                    return HttpResponseRedirect('/user/'+str(user.userid))
        context = {'form':form, 'already':True}
        return render(request, 'user/connection.html', context)

    context = {'form':form, 'already':already}
    return render(request, 'user/connection.html', context)

#page where you can create a new cat
def add(request,user_id):
    form = Catform()
    if request.method == 'POST':
        form = Catform(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.userid = User.objects.get(userid = user_id)
            result.save()
            return HttpResponseRedirect('/user/'+str(user_id))
    context = {'form':form, 'userid':user_id}
    return render(request, 'cat/add.html', context)

#page where you can edit a cat
def edit(request, user_id, cat_id):
    cat = Cat.objects.get(catid=cat_id)
    form = Catform(instance=cat)
    if request.method == 'POST':
        form = Catform(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.catid = cat_id
            result.userid = User.objects.get(userid = user_id)
            result.save()
            return HttpResponseRedirect('/user/'+str(user_id))
    return render(request,'cat/edit.html',{'form': form, 'userid':user_id})

#page where you can delete a cat
def delete(request, id, user_id):
  cat = Cat.objects.get(catid=id)
  cat.delete()
  return HttpResponseRedirect('/user/'+str(user_id))

#page where you can create a new account
def signin(request):
    already = False #same process as above if the email already exists
    form = totalUserform()
    if request.method == 'POST':
        form = totalUserform(request.POST)
        if form.is_valid():
            clear = form.cleaned_data
            if User.objects.filter(email=clear['email']).exists():
                already = True
            else:
                form.save()
                print("ca passe ici ")
                return HttpResponseRedirect('../')
    return render(request,'user/signin.html',{'form': form, 'already':already})

#page where you can delete an account
def udelete(request, user_id):
    user = User.objects.get(userid=user_id)
    user.delete()
    return HttpResponseRedirect('../../')

#page where you can edit an account
def uedit(request, user_id):
    user = User.objects.get(userid=user_id)
    form = editUserform(instance=user)
    if request.method == 'POST':
        form = editUserform(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.userid = user_id
            result.save()
            return HttpResponseRedirect('/user/'+str(user_id))
    return render(request,'user/uedit.html',{'form': form, 'userid':user_id})

