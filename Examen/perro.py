import Animales
class Perro(Animales.Animal):
    def Alimentar(self,tipoalimento,cantidadalimento):
        if(tipoalimento.lower()=='carne'):
            self.cantidadalimento+=cantidadalimento
            self.tipoalimento=tipoalimento

    def beber(self,cantidadagua):
        self.cantidadagua+=cantidadagua
        print('El perro tiene {0} litros de agua'.format(self.cantidadagua))
