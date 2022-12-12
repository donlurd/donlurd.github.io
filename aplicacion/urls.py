from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('categoria_list',views.categoria_list,name='categoria_list'),
    path('marca_list',views.marca_list,name='marca_list'),
    path('tienda_list',views.tienda_list,name='tienda_list'),
    path('categoria_tienda_list/<int:cat_id>',views.categoria_tienda_list,name='categoria_tienda_list'),
    path('marca_tienda_list/<int:marca_id>',views.marca_tienda_list,name='marca_tienda_list'),
    path('tienda/<str:slug>/<int:id>',views.tienda_detalle,name='tienda_detalle'),
    path('search',views.search,name='search'),
    path('filter-data',views.filter_data,name='filter_data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)