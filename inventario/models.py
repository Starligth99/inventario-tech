from django.db import models

class Categoria(models.Model):
    id = models.CharField(primary_key=True)
    name = models.TextField(max_length=80, unique=True)
    description = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)

class Meta:
    db_table = 'categoria'

def __str__(self):
    return self.name

class Marca(models.Model):
    id = models.CharField(primary_key=True)
    nombre = models.TextField(max_length=80, unique=True)
    sitio_web = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'marca'

    def __str__(self):
        return self.name    

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=50, unique=True)
    name=models.CharField(max_length=120)
    description=models.TextField(blank=True, null=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='productos')
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE, related_name='productos')
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True) 

    class Meta:
        db_table = 'producto'

    def __str__(self):
        return self.nombre
    
class Almacen(models.Model):
    id = models.CharField(primary_key=True)
    nombre = models.CharField(max_length=80, unique=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)


    class Meta:
        db_table = 'almacen'

    def __str__(self):
        return self.name
    
class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, related_name='inventarios')
    almacen = models.ForeignKey('Almacen', on_delete=models.CASCADE, related_name='inventarios')
    cantidad = models.IntegerField()
    stock_minimo = models.IntegerField(default=0)
    stock_maximo = models.IntegerField(default=0)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'inventario'

    def __str__(self):
        return f"{self.producto.name} - {self.almacen.nombre} - Cantidad: {self.cantidad}"
