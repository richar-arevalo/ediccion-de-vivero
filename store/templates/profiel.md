{% extends 'base.html' %}
{% block content %}
<div class="container mt-1">
    <div class="row">
        <div class="col-md-6">
            <!-- offset-md-1 -->
            <div class="card shadow">
                <div class="card-header bg-success text-white">
                    <div class="d-flex align-items-center gap-2">
                        <!-- Icono -->
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-person-fill" viewBox="0 0 16 16">
                            <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6" />
                        </svg>
                        <!-- Título -->
                        <h3 class="mb-0">Perfil de Usuario</h3>
                    </div>
                </div>
                <div class="card-body">
                    <p class="text-center">Bienvenido, <strong>{{ user.first_name }} {{ user.last_name }}</strong></p>
                    <hr>
                    <div class="row">
                        <div class="col-md-6">
                            <p><strong>Nombre de usuario:</strong> {{ user.username }}</p>
                            <p><strong>Correo electrónico:</strong> {{ user.email }}</p>
                        </div>
                        <div class="col-md-6">
                            <p><strong>Nombre:</strong> {{ user.first_name }}</p>
                            <p><strong>Apellido:</strong> {{ user.last_name }}</p>
                        </div>
                    </div>
                    <hr>
                    <div class="text-center">
                        
                        <a href="" class="btn btn-secondary">Editar Perfil</a>
                        <a href="{% url 'logout' %}" class="btn btn-danger">Cerrar Sesión</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<div class="container mt-1">
    <div class="">
        <div class="col-md-6 offset-md-4">
            <h3>Mis compras</h3>
        </div>
    </div>
</div>
{% endblock content %}
