class Carro:
    def __init__(self,placa,modelo,color,fecha_entrada,hora_entrada):
        self.placa = placa
        self.modelo = modelo 
        self.color = color
        self.fecha_entrada = fecha_entrada
        #self.fecha_salida = fecha_salida
        self.hora_entrada = hora_entrada

    def get_placa(self):
        return self.placa
    def set_placa(self,nueva_placa):
        self.placa = nueva_placa

    def get_modelo(self):
        return self.modelo
    def set_modelo(self,nuevo_modelo):
        self.modelo = nuevo_modelo

    def get_color(self):
        return self.color
    def set_color(self,nueva_color):
        self.color = nueva_color

    def get_fecha_entrada(self):
        return self.fecha_entrada
    def set_fecha_entrada(self,nueva_fecha_entrada):
        self.fecha_entrada = nueva_fecha_entrada

    #def get_fecha_salida(self):
       # return self.fecha_salida
    #def set_fecha_salida(self,nueva_fecha_salida):
       # self.fecha_salida = nueva_fecha_salida

    def get_hora_entrada(self):
        return self.hora_entrada
    def set_hora_entrada(self,nueva_hora_entrada):
        self.hora_entrada = nueva_hora_entrada



    def ver_info(self):
        info = f"la placa es: {self.placa}\n - Modelo es:{self.modelo}\n - El color es:  {self.self_color}\n - la fecha de ingreso es: {self.fecha_entrada}\n -la hora de ingreso es: {self.hora_entrada}"
        return info

    
