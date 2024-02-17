import msvcrt
class Nodo(): #Se crea el Nodo
    def __init__(self, datoN,datoA,datoC): #Metodo consutructor al cual le vamos a pasar los datos
        self.datoN=datoN #Hacemos referencia al dato
        self.datoA=datoA #Hacemos referencia al dato
        self.datoC=datoC #Hacemos referencia al dato
        self.siguiente=None #Apuntador Siguiente que sera Vacia(None)
        self.anterior=None #Apuntador Siguiente que sera Vacia(None)

class listaDobleEnlazada(): #Creamos nuetra Lista Doblemente Enlazada
    def __init__(self): #Metodo constructor para los Nodos
        self.primero=None #Hacemos referencia de que el primero estara Vacia(none)
        self.ultimo=None #Hacemos referencia de que el primero estara Vacia(none)
        self.size=0 #Tamaño de la Lista Doblemente Enlazada

    def vacia(self): #Metodo constructor vacio
        return self.primero==None #Validamos si nuestra lista esta vacia cuando primero esta vacio

    def agregar_final(self,datoN,datoA,datoC): #Metodo constructor de Agregar los Nodos al Final de la lista
        if self.vacia(): #Comprobamos si la lista esta vacia
            self.primero=self.ultimo=Nodo(datoN,datoA,datoC) #Agregamos el Nodo apuntando a primero y ultimo
            print()
            print("---------------------------------")
            print("Agregado al Final")
        else: #La lista no esta vacia
            aux=self.ultimo #Almacenos el ultimo nodo en una variable temporal
            self.ultimo=aux.siguiente=Nodo(datoN,datoA,datoC) #Apuntamos el ultimo nodo al nuevno nodo como su siguiente y de que sera el ultimo
            self.ultimo.anterior=aux #Apuntamos el ultimo nodo al nodo anterior
            print()
            print("---------------------------------")
            print("Agregado al Final")
        self.size+=1

    def agregar_inicio(self,datoN,datoA,datoC): #Metodo constructor de Agregar los Nodos al Inicio de la lista
        if self.vacia(): #Comprobamos si la lista esta vacia
            self.primero=self.ultimo=Nodo(datoN,datoA,datoC) #Agregamos el Nodo apuntando a primero y ultimo
            print()
            print("---------------------------------")
            print("Agregado al Inicio")
        else: #La lista no esta vacia
            aux=Nodo(datoN,datoA,datoC) #Almacenamos los datos en una variable temporal
            aux.siguiente=self.primero #Apuntamos el nuevo nodo al primer nodo como su siguiente
            self.primero.anterior=aux #Apuntamos el primer nodo al nuevo nodo como su anterior
            self.primero=aux #Ahora hacemos de que el nodo nuevo pase hacer el primero
            print()
            print("---------------------------------")
            print("Agregado al Inicio")
        self.size+=1

    def eliminar_inicio(self): #Metodo constructor eliminar inicio
        if self.vacia(): #Validando si la lista esta vacia
            print("Esta vacia") 
        elif self.primero.siguiente==None: #Si solo hay un nodo en la lista
            self.primero=self.ultimo=None #primero y ultimo sera igual a none
            print("Primer Nodo Eliminado")
            self.size=0 #Valor de lalista a 0
        else: #La lista tiene varios nodos
            self.primero=self.primero.siguiente #Colocando como primero al nodo siguiente del nodo
            self.primero.anterior=None #El anterior del primer nodo sera none
            print("Primer Nodo Eliminado")
            self.size-=1 #Reduciendo el valor de la lista

    def eliminar_final(self): #Metodo constructor para eliminar final
        if self.vacia(): #Si la lista esta vacia
            print("Esta vacia")
        elif self.primero.siguiente==None: #Si la lista tiene un solo nodo
            self.primero=self.ultimo=None #primero y ultimo sera igual a none
            print("Nodo Final Eliminado")
            self.size=0 #Valor de la lista a 0
        else: #La lista tiene varios nodos
            self.ultimo=self.ultimo.anterior #Colocando como ultimo al nodo anterior del nodo
            self.ultimo.siguiente=None #El anterior del primer nodo sera none
            print("Nodo Final Eliminado")
            self.size-=1 #Reduciendo el valor de la lista
        
    def recorrer_inicio(self): #Metodo constructor para recorrer la lista de Inicio a Fin
        aux=self.primero #Almacenando al primero en una variable temporal
        while aux: #Se repetira mientras sea verdadero
            print(aux.datoN,aux.datoA,aux.datoC) #Imprimir los datos
            aux=aux.siguiente #Almacenando el nodo siguiente a la variable temporal

    def recorrer_fin(self): #Metodo constructor para recorrer la lista de Fin a Inicio
        aux=self.ultimo #Almacenando al ultimo en una variable temporal
        while aux: #Se repetira mientras sea verdadero
            print(aux.datoN,aux.datoA,aux.datoC) #Imprimir los datos
            aux=aux.anterior #Almacenando el nodo anterior a la variable temporal

    def size(self): #Metodo constructor para el temaño de la lista
        return self.size #retornando el valor/tamaño de la lista

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