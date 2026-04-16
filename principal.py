from base_datos import Base_datos
from controlador import Controlador
from interfaz_vista import Ventana

obj_vista = Ventana()
obj_controlador = Controlador(obj_vista)

obj_controlador.recibir_datos_carro()
obj_controlador.confirmar_guardado()

obj_db = Base_datos()
obj_db.ver_datos()

"""
#controlador manipula y actualiza las vista
vista el que manda y recibe la informacion al Controlador
controlado recibe y crea instancias los objetos
los modelos mandan informacion a la base de Base_datos
"""