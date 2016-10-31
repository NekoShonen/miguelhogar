from django.shortcuts import render
from .models import Producto
from .models import Rubro
from .models import Seleccionados


def paginaPrincipal(request):

    rubros= Rubro.objects.all()
    #seleccionados_r = Seleccionados.objects.all()
    #productos_r=Producto.objects.filter(producto_pk=seleccionados_r.productos )

    #persona_r = Persona.objects.get(id=idPersona)
    #capacitaciones_r = Capacitacion.objects.filter(cargos__id=persona_r.cargo)

    seleccionados=Seleccionados.objects.all()

    return render(request, 'miguelHogarSyte/Principal.html', {'rubros':rubros,'seleccionados':seleccionados})

def productosElectrodomesticos(request):
    productos=Producto.objects.all()
    #productos= Producto.objects.filter(rubro__nombre='Electrodomesticos')
    rubros= Rubro.objects.all()

    return render(request, 'miguelHogarSyte/rubro.html', {'productos': productos,'rubros':rubros})

# Create your views here.
