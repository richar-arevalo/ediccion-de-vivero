from django.urls.conf import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('store/', views.store, name='store'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('register/', views.register, name='register'),
    path('agregar/<int:product_id>/', views.agregar_compras, name='agregar_compras'),
]
