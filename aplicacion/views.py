from django.shortcuts import render
from .models import Categoria,Marca,Tienda,Banner

from django.http import JsonResponse,HttpResponse
from django.template.loader import render_to_string
# Create your views here.

# Pagina Principal

def home(request):
    banners = Banner.objects.all().order_by('-id')
    data = Tienda.objects.filter(es_destacado=True).order_by('-id')
    return render(request,'index.html',{'data':data,'banners':banners})

# Categorias
def categoria_list(request):
    data = Categoria.objects.all().order_by('-id')
    return render(request,'categoria_list.html',{'data' :data})

# Marcas
def marca_list(request):
    data = Marca.objects.all().order_by('-id')
    return render(request,'marca_list.html',{'data' :data})

# lista de tiendas

def tienda_list(request):
    data = Tienda.objects.all().order_by('-id')
    cats = Tienda.objects.distinct().values('categoria__title','categoria__id')
    marcs = Tienda.objects.distinct().values('marca__title','marca__id')
    return render(request,'tienda_list.html',
        {#agregar aqui datam que luego estara en tieda_listam para que la maneje la pagina
            'data' :data,
            'cats' :cats,
            'marcs':marcs, 
        }
        )

# lista tiendas segun categoria

def categoria_tienda_list(request,cat_id):
    categoria = Categoria.objects.get(id=cat_id)
    data = Tienda.objects.filter(categoria=categoria).order_by('-id')
    cats = Tienda.objects.distinct().values('categoria__title','categoria__id')
    marcs = Tienda.objects.distinct().values('marca__title','marca__id')
    return render(request,'categoria_tienda_list.html',{
        'data':data,
        'cats' :cats,
        'marcs':marcs, 
        })

# lista tiendas segun marca

def marca_tienda_list(request,marca_id):
    marca = Marca.objects.get(id=marca_id)
    data = Tienda.objects.filter(marca=marca).order_by('-id')
    cats = Tienda.objects.distinct().values('categoria__title','marca__id')
    marcs = Tienda.objects.distinct().values('marca__title','marca__id')
    return render(request,'marca_tienda_list.html',{
        'data':data,
        'cats' :cats,
        'marcs':marcs, 
        })

# Detalle Tiends

def tienda_detalle(request,slug,id):
    tienda = Tienda.objects.get(id=id)
    return render(request,'tienda_detalle.html',{'data':tienda})

# buscar

def search(request):
    q=request.GET['q']
    data = Tienda.objects.filter(title__icontains=q).order_by('-id')
    return render(request,'search.html',{'data':data})

# data filtro

def filter_data(request):
    categorias = request.GET.getlist('categoria[]')
    marca = request.GET.getlist('marca[]')
    allTienda = Tienda.objects.all().order_by('-id')
    if len(categorias)>0:
        allTienda=allTienda.filter(categoria__id__in=categorias).distinct()
    if len(marca)>0:
        allTienda=allTienda.filter(marca__id__in=marca).distinct()
    t=render_to_string('ajax/tienda-list.html',{'data':allTienda})
    return JsonResponse({'data':t})

















