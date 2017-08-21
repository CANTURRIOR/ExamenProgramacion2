import conejo
import elefante
import perro

def ConstruirConejo(CantidadReproduccion,CantidadAnimales):
    Conejo=conejo.Conejo(CantidadReproduccion,CantidadAnimales)
    return Conejo

def ConstruirElefante(CantidadReproduccion,CantidadAnimales):
    Elefante=elefante.Elefante(CantidadReproduccion,CantidadAnimales)
    return Elefante

def ConstruirPerro(CantidadReproduccion,CantidadAnimales):
    Perro=perro.Perro(CantidadReproduccion,CantidadAnimales)
    return Perro

def ImprimirMenu():
    print('1 Agregar Nuevo Animal\n2 Animal pregnados\n3 Alimentar Animales\n4 Dar de beber')
    print('5 Salir')
    accion= int(input('Ingrese el numero de la accion que desea hacer: '))
    return accion

def ImprimirAnimales():
    print('1 Conejo\n2 Elefante\n3 Perro')
    accion=int(input('Ingrese el numero de la accion que desea hacer: '))
    return accion

conejoconstruido=False
elefanteconstruido=False
perroconstruido=False
salir=False

while not salir:
    accion=ImprimirMenu()
    if(accion==1):
        tipoanimal=ImprimirAnimales()
        if(tipoanimal==1):
            cantidadanimales=int(input('Ingrese la cantidad de conejos que tiene '))
            cantidadreproduccion=int(input('Ingrese la cantidad de animales por parto que puede tener un conejo '))
            conejoconstruido=ConstruirConejo(cantidadreproduccion,cantidadanimales)
        elif(tipoanimal==2):
            cantidadanimales=int(input('Ingrese la cantidad de elefantes que tiene '))
            cantidadreproduccion=int(input('Ingrese la cantidad de animales por parto que puede tener un elefante '))
            elefanteconstruido=ConstruirElefante(cantidadreproduccion,cantidadanimales)
        elif(tipoanimal==3):
            cantidadanimales=int(input('Ingrese la cantidad de perros que tiene '))
            cantidadreproduccion=int(input('Ingrese la cantidad de animales por parto que puede tener un perro '))
            perroconstruido=ConstruirPerro(cantidadreproduccion,cantidadanimales)
        else:
            print('El comando ingresado no se reconoce')
    elif(accion==2):
        tipoanimal=ImprimirAnimales()
        if(tipoanimal==1):
            if(conejoconstruido!=False):
                cantidadanimalespreniados=int(input('Ingrese la cantida de animales pregnados '))
                conejoconstruido.Reproduccion(cantidadanimalespreniados)
            else:
                print('No tiene conejos en su granja')
        elif(tipoanimal==2):
            if(elefanteconstruido!=False):
                cantidadanimalespreniados=int(input('Ingrese la cantida de animales pregnados '))
                elefanteconstruido.Reproduccion(cantidadanimalespreniados)
            else:
                print('No tiene elefantes en su granja')
        elif(tipoanimal==3):
            if(perroconstruido!=False):
                cantidadanimalespreniados=int(input('Ingrese la cantida de animales pregnados '))
                perroconstruido.Reproduccion(cantidadanimalespreniados)
            else:
                print('No tiene perros en su granja')


    elif(accion==3):
        tipoanimal=ImprimirAnimales()
        if(tipoanimal==1):
            if(conejoconstruido!=False):
                tipoalimento=input('Ingrese el tipo de alimento que da a los conejos ')
                cantidadalimento=int(input('Ingrese la cantidad de alimento '))
                conejoconstruido.Alimentar(tipoalimento,cantidadalimento)
            else:
                print('No tiene conejos en su granja')
        elif(tipoanimal==2):
            if(elefanteconstruido!=False):
                tipoalimento=input('Ingrese el tipo de alimento que da a los elefantes ')
                cantidadalimento=int(input('Ingrese la cantidad de alimento '))
                elefanteconstruido.Alimentar(tipoalimento,cantidadalimento)
            else:
                print('No tiene elefantes en su granja')
        elif(tipoanimal==3):
            if(perroconstruido!=False):
                tipoalimento=input('Ingrese el tipo de alimento que da a los perros ')
                cantidadalimento=int(input('Ingrese la cantidad de alimento '))
                perroconstruido.Alimentar(tipoalimento,cantidadalimento)
            else:
                print('No tiene perros en su granja')
        else:
            print('No se reconoce el comando ingresado')
    elif(accion==4):
        tipoanimal=ImprimirAnimales()
        if(tipoanimal==1):
            if(conejoconstruido!=False):
                print('No pude dar de beber a los conejos')
            else:
                print('No tiene conejos en su granja')
        elif(tipoanimal==2):
            if(elefanteconstruido!=False):
                cantidadagua=int(input('Ingrese la cantidad de agua para los elefantes '))
                elefanteconstruido.TomarAgua(cantidadagua)
            else:
                print('No tiene elefantes en su granja')
        elif(tipoanimal==3):
            if(perroconstruido!=False):
                cantidadagua=int(input('Ingrese la cantidad de agua para los perros '))
                perroconstruido.beber(cantidadagua)
            else:
                print('No tiene elefantes en su granja')
        else:
            print('Comando ingresado desconocido')
    elif(accion==5):
        salir=True
    else:
        print('El comando Ingresado no se reconoce')
