from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm, AdminLoginForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from App_Auth import models as App_AuthModel
from App_Auth import forms as App_AuthForms
from django.db.models import Subquery, OuterRef, Value
from django.db.models.functions import Coalesce



# 404 Error
def handle_not_found(request,exception):
	return render(request, "App_Auth/404.html", status=404)

# ######### +++++++++++++++++++++ ADMIN PANEL +++++++++++++++++++++ #########

def is_admin(user):
    return user.is_authenticated and user.is_staff and user.is_superuser

def admin_logout_view(request):
    logout(request)
    return redirect('App_Auth:login')  

def admin_login_view(request):
    if request.method == 'POST':
        form = AdminLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                if user.is_staff and user.is_superuser:  
                    login(request, user)
                    return redirect('App_Auth:dashboard')  
                else:
                    messages.error(request, 'Access denied. Admin only.')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = AdminLoginForm()
    return render(request, 'App_Admin/login.html', {'form': form})



# dashboard
@login_required(login_url='App_Auth:login')
def dashboard(request):
    if not request.user.is_staff or not request.user.is_superuser:
        messages.error(request, 'Access denied. Admin only.')
        return redirect('App_Auth:login')
    
    return render(request, "App_Auth/dashboard.html")
