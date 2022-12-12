from django.db import models
from django.utils.html import mark_safe

# Banner

class Banner(models.Model):
    img = models.ImageField(upload_to="banner_imgs/")
    alt_text = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural='1. Banners'
    
    def image_tag(self): #se vea la imagen en el admin
        return mark_safe('<img src="%s" width="100" />' % (self.img.url))

# Categorias
class Categoria(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cat_imgs/")

    class Meta:
        verbose_name_plural='2. Categorias'

    def image_tag(self): #se vea la imagen en el admin
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

# Marcas
class Marca(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="marca_imgs/")
    
    class Meta:
        verbose_name_plural='3. Marcas'

    def image_tag(self): #se vea la imagen en el admin
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))    

    def __str__(self):
        return self.title

## si deseo agregar mas cartegorias repita lo anterior
## recuerda pasar estos modelos a admin.py

# Producto Model

class Tienda(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="tienda_imgs/")
    slug = models.CharField(max_length=400)
    details= models.TextField()
    specs = models.TextField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)    
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)
    status=models.BooleanField(default=True) #para controlarlo desde aca si aparece la tienda o no
    #agregar datos como telefono, redsociales y fotos
    es_destacado=models.BooleanField(default=False) # que sean destacados
    
    class Meta:
        verbose_name_plural='4. Tiendas'
    
    def image_tag(self): #se vea la imagen en el admin
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

# Tienda atributo (si quiero agregar variaciones)

class TiendaAtributo(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)    
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='5. Atributos tiendas'

    def __str__(self):
        return self.tienda.title