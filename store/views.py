from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, CustomAuthenticationForm
from .models import Producto, Compra
# Create your views here.

def store(request):
    products = Producto.objects.all()
    return render(request, 'store.html', {'products': products})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Crear un nuevo usuario
            user = User.objects.create_user(
                username=form.cleaned_data['email'],  # Puedes usar el correo como username
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('profile') 
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f"¡Bienvenido, {user.username}!")
            return redirect('profile')  # Cambia 'home' a la vista principal de tu aplicación
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# vista del perfil
def user_profile(request):
    if not request.user.is_authenticated:
        # Redirige al inicio de sesión si el usuario no está autenticado
        messages.warning(request, "Debes iniciar sesión para acceder a tu perfil.")
        return redirect('login')

    # Si está autenticado, procesa normalmente
    compras = request.user.compras.all()
    return render(request, 'user_profile.html', {'compras': compras})


# @login_required
# def user_profile(request):
#     compras = request.user.compras.all()  # Ajusta según el modelo de tus compras
#     return render(request, 'user_profile.html', {'compras': compras})

@login_required
def agregar_compras(request, product_id):
    producto = get_object_or_404(Producto, id=product_id)
    if producto.stock <=0:
        messages.error(request, "Este producto esta agotado")
        return redirect('store')
    
    compra, created = Compra.objects.get_or_create(
        user=request.user,
        product=producto
    )
    
    compra.quantity += 1
    compra.save()
    producto.stock -= 1
    producto.save()
    
    messages.success(request, f"Has agregado {producto.name} a tus compras.")
    return redirect('store')
            


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "¡Tu cuenta ha sido creada exitosamente!")
#             return redirect('login') 
#     else:
#         form = UserCreationForm()
    
#     return render(request, 'register.html', {'form': form})





