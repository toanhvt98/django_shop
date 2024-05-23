from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.template.loader import render_to_string
from .helper import get_static_image_files
from .forms import LoginForm,RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import permission_required

# for all user
#########################################################################
def index_page(request):
    return render(request, 'shop/index_page.html')

def product_page(request):
    return render(request, 'shop/product_page.html')

def electronics_products_page(request):
    return render(request,'shop/electronics_products_page.html')
def shoe_products_page(request):
    return render(request,'shop/shoe_products_page.html')
def clothes_products_page(request):
    return render(request,'shop/clothing_products_page.html')
#########################################################################


# for admin
#########################################################################
@permission_required('auth.is_superuser')
def admin_management(request):
    return render(request,'shop/admin/management.html')
@permission_required('auth.is_superuser')
def admin_dashboard(request):
    return render(request,'shop/admin/dashboard.html')
@permission_required('auth.is_superuser')
def admin_management_electronics_products(request):
    return render(request,'shop/admin/management/electronics_products.html')
@permission_required('auth.is_superuser')
def admin_management_clothing_products(request):
    return render(request,'shop/admin/management/clothing_products.html')
@permission_required('auth.is_superuser')
def admin_management_shoe_products(request):
    return render(request,'shop/admin/management/shoe_products.html')
#########################################################################


# user actions
#########################################################################
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if remember_me:
                    request.session.set_expiry(86400 * 30)
                else:
                    request.session.set_expiry(0)
                return redirect("product") 
            else:
                error_message = 'Username or password is incorrect!!'
                return render(request, 'shop/login.html', {'form': form, 'login_error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'shop/login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            

            if User.objects.filter(username=username).exists():
                return render(request, 'shop/register.html', {'form': form, 'register_error_message': 'This username already exists.'})
            try:
                validate_password(password)
            except:
                return render(request, 'shop/register.html', {'form': form, 'register_error_message': 'Passwords must be at least 6 characters'})
            if password != re_password:
                return render(request, 'shop/register.html', {'form': form, 'register_error_message': 'Re-password not matched'})
            user = User.objects.create_user(username=username, password=password)
            user.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('product')
    else:
        form = RegisterForm()
    return render(request, 'shop/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect("/")
#########################################################################
    