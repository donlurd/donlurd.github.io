from .models import Tienda, TiendaAtributo
def get_filters(request):
    cats = Tienda.objects.distinct().values('categoria__title','categoria__id')
    marcs = Tienda.objects.distinct().values('marca__title','marca__id')
    data={
        'cats' :cats,
        'marcs':marcs,
    }
    return data 
