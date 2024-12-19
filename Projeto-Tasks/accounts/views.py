from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        user_form = CustomUserCreationForm(request.POST)  # Use o formulário personalizado
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = CustomUserCreationForm()  # Use o formulário personalizado
    return render(request, 'register.html', {'user_form': user_form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('tasks_list')
    if request.method =='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tasks_list')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('tasks_list')