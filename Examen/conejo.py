import Animales
class Conejo(Animales.Animal):
    def Alimentar(self,tipoalimento,cantidadalimento):
        if(tipoalimento.lower()=='pasto'):
            self.cantidadalimento+=cantidadalimento
            self.tipoalimento=tipoalimento

    def Correr(self):
        if(self.cantidadalimento>0):
            self.cantidadalimento-=1
            print(self.cantidadalimento)
        else:
            print('Estoy cansado y hambriento')
