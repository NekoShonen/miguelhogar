<!DOCTYPE html>
<html lang="en">
{% load staticfiles %}
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

  <style>
  .carousel-inner > .item > img,
  .carousel-inner > .item > a > img {
      width: 50%;
      height: 100%;
      margin: auto;
  }
  </style>

<link href="{% static 'miguelHogarSyte/estilo.css' %}" rel="stylesheet" type="text/css">


</head>
<body>

<div class="divlogo">

<img class="logo" src="../../static/img/logo.jpg">


</div>

<br>
<div name="rubros" class="rubros">
Rubros
<list>
{% for rubro in rubros %}
    <a href="/{{rubro.nombre}}"><li>{{rubro.nombre}}</li></a>
{% endfor %}
</list>
</div>

</body>

</html>