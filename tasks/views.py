from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Tasks
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    tasks=Tasks.objects.filter(user=request.user)
    return render(request, 'tasks/home.html',{'tasks':tasks})


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'tasks/signup.html', {
                'error': 'Username already exists. Please choose another one.'
            })

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect('home')

    return render(request, 'tasks/signup.html')


def user_login(request):
    if request.method== "POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,
                          username=username,
                          password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
    return render(request,'tasks/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')



def add_task(request):
    if request.method == "POST":
        title=request.POST['title']

        Tasks.objects.create(user=request.user,
                             title=title,
                             completed=False)
        
        return redirect('home')
    
    return render(request, 'tasks/home.html')


def delete_task(request, id):
    task=Tasks.objects.get(id=id)

    task.delete()

    return redirect('home')



def update_task(request, id):
    task=Tasks.objects.get(id=id)

    if request.method == "POST":
        task.title=request.POST['title']
        task.save()

        return redirect('home')
    

def complete_task(request, id):
    task=Tasks.objects.get(id=id)

    if request.method == "POST":
        task.completed = not task.completed
        task.save()

    return redirect('home')

