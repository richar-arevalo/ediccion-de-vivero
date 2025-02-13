<style>
  .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .text-container {
    max-width: 500px;
    text-align: justify;
  }

  .title {
    font-size: 2.5rem;
    color: #007bff;
    margin-bottom: 15px;
  }

  .sub {
    font-size: 1.5rem;
    color: #333;
    margin-bottom: 10px;
  }

  .description {
    font-size: 1rem;
    color: #666;
    margin-bottom: 20px;
  }

  .btn-secondary {
    background-color: #007bff;
    color: #fff;
    padding: 10px 20px;
    border-radius: 5px;
    text-decoration: none;
    font-size: 1rem;
    transition: background-color 0.3s ease;
  }

  .btn-secondary:hover {
    background-color: #0056b3;
  }

  .fondo {
    width: 100%;
    max-width: 720px; /* ajusta según sea necesario */
    height: auto;
  }
</style>

<div class="container p-4">
  <div class="text-container">
    <h1 class="title">Vida verde</h1>
    <h3 class="sub">Encuentra gran variedad de plantas</h3>
    <p class="description">
      Invernadero Vida verde desde 2015 ofrece una gran <br />
      variedad de plantas frutales
    </p>
    <a href="#" class="btn btn-secondary">Productos</a>
  </div>
  <div class="flex-grow-1 mt-4 mt-md-0 ms-md-4">
    <div class="fs-4">
      <img
        src="{% static 'img/back1.png' %}"
        alt="fondo"
        class="img-fluid fondo"
      />
    </div>
  </div>
</div>
{% include 'card.html' %} {% include 'info.html' %}