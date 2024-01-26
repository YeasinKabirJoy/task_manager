from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .forms import CustomUserCreationForm
class Login(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('all-task')
        else:
            return render(request, 'user/login.html')
    def post(self,request):

            username = request.POST['username']
            password = request.POST['password']
            try:
                user = User.objects.get(username=username)
            except:
                return redirect('login')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('all-task')
            else:
                return redirect('login')


class Registration(View):
    def get(self,request):
        form = CustomUserCreationForm()
        context={
            "form": form
        }
        return render(request,'user/registration.html',context)

    def post(self,request):
        print(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            try:
                User.objects.get(username=user.username)
                form = CustomUserCreationForm(request.POST)
                context = {
                    'form': form
                }
                return render(request, 'user/registration.html', context)
            except:
                user.save()
                login(request, user)
                return redirect('all-task')
        else:
            return redirect('register')


class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')


