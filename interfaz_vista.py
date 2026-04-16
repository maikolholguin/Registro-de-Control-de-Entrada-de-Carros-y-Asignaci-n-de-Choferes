class Ventana:
    def __init__(self):
        self.titulo= "Registro de datos"

    def tomar_datos_carro(self):
        placa = input("dijite la placa: ")
        modelo = input("dijite el modelo: ")
        color = input("dijite el color: ")
        fecha_entrada = input("dijite la fecha de entrada: ")
        hora_entrada = input("dijite la hora de entrada: ")

        datos = [placa,modelo,color,fecha_entrada,hora_entrada]
        return datos

    def tomar_datos_chofer(self):
        pass

    def visualizar_datos(self):
        pass

    def hacer_mensaje(self,dato):
        if dato :
            print("usuario creado en el sistema")
        else: print("Error... usuario no creado...")