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
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import permission_required
from django.views.decorators.http import require_GET
from django.utils.translation import gettext as _
from django.utils.translation import get_language,activate,gettext
# for all user
#########################################################################


def home_page(request):

    return render(request, 'shop/home_page.html')

def product_page(request):
    return render(request, 'shop/products/index_product_page.html')

@require_GET
def electronics_products_page(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render(request, 'shop/products/electronics_products_page.html').content.decode('utf-8')
        return JsonResponse({'html': html})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@require_GET
def clothing_products_page(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render(request, 'shop/products/clothing_products_page.html').content.decode('utf-8')
        return JsonResponse({'html': html})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@require_GET
def shoe_products_page(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render(request, 'shop/products/shoe_products_page.html').content.decode('utf-8')
        return JsonResponse({'html': html})
    return JsonResponse({'error': 'Invalid request'}, status=400)
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
                if user.is_staff:
                    return redirect(reverse('admin:index'))
                return redirect("product_page") 
            else:
                error_message = 'Username or password is incorrect!!'
                return render(request, 'shop/login_page.html', {'form': form, 'login_error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'shop/login_page.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            

            if User.objects.filter(username=username).exists():
                return render(request, 'shop/register_page.html', {'form': form, 'register_error_message': 'This username already exists.'})
            try:
                validate_password(password)
            except:
                return render(request, 'shop/register_page.html', {'form': form, 'register_error_message': 'Passwords must be at least 6 characters'})
            if password != re_password:
                return render(request, 'shop/register_page.html', {'form': form, 'register_error_message': 'Re-password not matched'})
            user = User.objects.create_user(username=username, password=password)
            user.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('product_page')
    else:
        form = RegisterForm()
    return render(request, 'shop/register_page.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect("/")
#########################################################################
    