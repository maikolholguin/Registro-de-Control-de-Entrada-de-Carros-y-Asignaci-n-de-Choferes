






class Base_datos:
    def __init__(self):
        self.lista_info = []

    def guardar_info(self,obj_carro,obj_chofer):
        #en los metos de base de datos ejecutar sql
        dato_carro = [obj_carro.get_placa(),obj_carro.get_modelo(),obj_carro.get_color(),obj_carro.get_fecha_entrada(),obj_carro.get_hora_entrada()]
        #dato_chofer = [obj_chofer.get_cedula(),obj_chofer.get_nombre()]
        datos_totales = [dato_carro]
        self.lista_info.append(datos_totales)

    def buscar_info(self):
        pass
    def ver_datos(self):
        print("esat pendiente por hacer")