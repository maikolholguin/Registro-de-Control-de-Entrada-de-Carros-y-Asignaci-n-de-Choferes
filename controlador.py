from carros import Carro
from base_datos import Base_datos


class Controlador:
    def __init__(self, obj_vista):
        self.obj_modelo = ""
        self.obj_vista=obj_vista
        self.obj_bd=Base_datos()



    def recibir_datos_carro(self):
        info_datos = self.obj_vista . tomar_datos_carro()
        print(info_datos)

        self.obj_modelo=Carro(info_datos[0],info_datos[1],info_datos[2],info_datos[3],info_datos[4])
        self.db.guardar_info(self.obj_modelo,self.chofer)

        
    def confirmar_guardado(self):
        #este true depende de la respuesta del modelo
        self.obj_vista.hacer_mensaje(True)