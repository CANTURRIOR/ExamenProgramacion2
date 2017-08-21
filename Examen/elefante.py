import Animales

class Elefante(Animales.Animal):
    def TomarAgua(self,cantidadagua):
        self.cantidadagua+=cantidadagua
        print('El elefante tiene {0} litros de agua'.format(self.cantidadagua))

    def Alimentar(self,tipoalimento,cantidadalimento):
        if(tipoalimento.lower()=='mani'):
            self.cantidadalimento+=cantidadalimento
        else:
            print('Solo me alimento de mani')
