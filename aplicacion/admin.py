from django.contrib import admin
from .models import	Banner,Categoria,Marca,Tienda,TiendaAtributo #agregar modelos creados aca en admin



class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text','img','image_tag')
admin.site.register(Banner,BannerAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(Categoria,CategoriaAdmin)

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(Marca,MarcaAdmin)

class TiendaAdmin(admin.ModelAdmin): #como lo veo en admin
    list_display=('id','title','status','categoria','image_tag','es_destacado')
    list_editable=('status','es_destacado')
admin.site.register(Tienda,TiendaAdmin)
# Register your models here.

# Tienda Atributos
class TiendaAtributoAdmin(admin.ModelAdmin):
    list_display=('id','tienda','marca','categoria')
admin.site.register(TiendaAtributo,TiendaAtributoAdmin)
