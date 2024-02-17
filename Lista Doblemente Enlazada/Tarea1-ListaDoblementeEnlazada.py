import msvcrt

class Nodo():
    def __init__(self, datoN,datoA,datoC):
        self.datoN=datoN
        self.datoA=datoA
        self.datoC=datoC
        self.siguiente=None
        self.anterior=None

class listaDobleEnlazada():
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.size=0

    def vacia(self):
        return self.primero==None

    def agregar_final(self,datoN,datoA,datoC):
        if self.vacia():
            self.primero=self.ultimo=Nodo(datoN,datoA,datoC)
            print()
            print("---------------------------------")
            print("Agregado al Final")
        else:
            aux=self.ultimo
            self.ultimo=aux.siguiente=Nodo(datoN,datoA,datoC)
            self.ultimo.anterior=aux
            print()
            print("---------------------------------")
            print("Agregado al Final")
        self.size+=1

    def agregar_inicio(self,datoN,datoA,datoC):
        if self.vacia():
            self.primero=self.ultimo=Nodo(datoN,datoA,datoC)
            print()
            print("---------------------------------")
            print("Agregado al Inicio")
        else:
            aux=Nodo(datoN,datoA,datoC)
            aux.siguiente=self.primero
            self.primero.anterior=aux
            self.primero=aux
            print()
            print("---------------------------------")
            print("Agregado al Inicio")
        self.size+=1

    def eliminar_inicio(self):
        if self.vacia():
            print("Esta vacia")
        elif self.primero.siguiente==None:
            self.primero=self.ultimo=None
            print("Primer Nodo Eliminado")
            self.size=0
        else:
            self.primero=self.primero.siguiente
            self.primero.anterior=None
            print("Primer Nodo Eliminado")
            self.size-=1

    def eliminar_final(self):
        if self.vacia():
            print("Esta vacia")
        elif self.primero.siguiente==None:
            self.primero=self.ultimo=None
            print("Nodo Final Eliminado")
            self.size=0
        else:
            self.ultimo=self.ultimo.anterior
            self.ultimo.siguiente=None
            print("Nodo Final Eliminado")
            self.size-=1
        
    def recorrer_inicio(self):
        aux=self.primero
        while aux:
            print(aux.datoN,aux.datoA,aux.datoC)
            aux=aux.siguiente

    def recorrer_fin(self):
        aux=self.ultimo
        while aux:
            print(aux.datoN,aux.datoA,aux.datoC)
            aux=aux.anterior

    def size(self):
        return self.size

lista=listaDobleEnlazada()

def menInserInicio():
    try:
        print("---------------------------------")
        datN=str(input("Ingresa el Nombre: "))
        datA=str(input("Ingresa el Apellido: "))
        datC=int(input("Ingresa el Carné: "))
        lista.agregar_inicio(datN,datA,datC)
        print("---------------------------------")
    except:
        print()
        print("Por favor ingrese caracteres correctos")
        print("Presione una tecla para continuar...")
        msvcrt.getch()

def menInserFinal():
    try:
        print("---------------------------------")
        datN=str(input("Ingresa el Nombre: "))
        datA=str(input("Ingresa el Apellido: "))
        datC=int(input("Ingresa el Carné: "))
        lista.agregar_final(datN,datA,datC)
        print("---------------------------------")
    except:
        print()
        print("Por favor ingrese caracteres correctos")
        print("Presione una tecla para continuar...")
        msvcrt.getch()

while True:
    print()
    print("|--------------------------------------------------|")
    print("|            LISTA DOBLEMENTE ENLAZADA             |")
    print("|--------------------------------------------------|")
    print()
    print("¿Que quieres realizar?")
    print("1) Insertar al Inicio")
    print("2) Insertar al Final")
    print("3) Eliminar Primer Nodo")
    print("4) Eliminar Ultimo Nodo")
    print("5) Imprimir de Inicio a Final")
    print("6) Imprimir de Final a Inicio")
    print("0) Salir")
    print()

    try:
        n=int(input("Ingresa la opcion: "))

        if n==1:
            menInserInicio()
        elif n==2:
            menInserFinal()
        elif n==3:
            print()
            print("---------------------------------")
            lista.eliminar_inicio()
            print("---------------------------------")
        elif n==4:
            print()
            print()
            print("---------------------------------")
            lista.eliminar_final()
            print("---------------------------------")
        elif n==5:
            print()
            print("---------------------------------")
            lista.recorrer_inicio()
            print("---------------------------------")
        elif n==6:
            print()
            print("---------------------------------")
            lista.recorrer_fin()
            print("---------------------------------")
        elif n==0:
            break
        print()
        print("Presione una tecla para continuar...")
        msvcrt.getch()
    except:
        print()
        print("Ingrese un numero del menu")
        print("Presione una tecla para continuar...")
        msvcrt.getch()