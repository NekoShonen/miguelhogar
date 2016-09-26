from django.shortcuts import render
from .models import Producto
def productos(request):
    productos= Producto.objects.filter(rubro__nombre='Electrodomesticos')
    return render(request, 'miguelHogarSyte/rubro.html', {'productos': productos})

# Create your views here.
