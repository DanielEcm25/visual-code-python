class Producto:
    def __init__(self, nombre, descripcion, precio, stock):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__stock = stock
    def actualizar_stock(self, cantidad):
        self.__stock -= cantidad
    def getNom(self):
        return self.__nombre
    def getDescripcion(self):
        return self.__descripcion
    def getPrecio(self):
        return self.__precio
    def getStock(self):
        return self.__stock
class Inventario(Producto):
    def __init__(self):
        self.productos = []
    def agregar_producto(self, producto):
        self.productos.append(producto)
    def actualizar_stock(self, nombre_producto, cantidad_vendida):
        for producto in self.productos:
            if producto.getNom() == nombre_producto:
                producto.actualizar_stock(cantidad_vendida)
                break
    def generar_informe(self):
        for producto in self.productos:
            print(f"\x1b[1;34mProducto:\x1b[0;37m {producto.getNom()}, \x1b[1;36m \nStock: \x1b[0;37m {producto.getStock()}")
class Venta(Producto):
    def __init__(self):
        self.productos_vendidos = []
    def agregar_producto_vendido(self, producto, cantidad):
        self.productos_vendidos.append((producto, cantidad))
    def calcular_total(self):
        total = 0
        for producto, cantidad in self.productos_vendidos:
            total += producto.getPrecio() * cantidad
        return total
def Authors():
    return """\n\x1b[1;32mHecho por:
\x1b[1;32m>\x1b[0;37mDiego Sánchez Cediel\x1b[0;37m
\x1b[1;32m>\x1b[0;37mHumberto Pinilla\x1b[0;37m
\x1b[1;32m>\x1b[0;37mWilliam Suárez\x1b[0;37m  
\x1b[1;32m>\x1b[0;37mDaniel Esteban Contreras\x1b[0;37m\n"""
prod1=Producto("Pistola de Agua","Pistola de Agua Nerf",40000,50)
prod2=Producto("Max Steel Turbo","Max Steel Turbo Ultimate Edition",20000,80)
prod3=Producto("Hot Wheels","BMW 2015 Hot Wheels",15000,10)
prod4=Producto("Peluche","Peluche de Algodon",14000,47)
inventario=Inventario()
inventario.agregar_producto(prod1)
inventario.agregar_producto(prod2)
inventario.agregar_producto(prod3)
inventario.agregar_producto(prod4)
venta=Venta()
venta.agregar_producto_vendido(prod1,2)
venta.agregar_producto_vendido(prod2,1)
venta.agregar_producto_vendido(prod3,3)
venta.agregar_producto_vendido(prod4,4)
total_venta=venta.calcular_total()
inventario.actualizar_stock("Pistola de Agua",14)
inventario.actualizar_stock("Max Steel Turbo",23)
inventario.actualizar_stock("Hot Wheels",9)
inventario.actualizar_stock("Peluche",36)
print(f"\n\x1b[1;36mTotal de la Venta:\x1b[0;37m {total_venta}\n")
inventario.generar_informe()
print(Authors())