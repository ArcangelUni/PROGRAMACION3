import msvcrt
import math
from math import sqrt

def convertir_a_binario (n1):
    
    if n1==0:
        return ""
    else:
        return convertir_a_binario(n1//2)+str(n1%2)

def contar_digitos(n2):
    if n2<10 and n2>=0:
        return 1
    elif n2<0:
        return "(Ingrese un numero entero positivo)"
    else:
        n2=n2/10
        return 1+contar_digitos(n2)


def raiz_cuadrada_entera(n3):
    global nn3
    nn3=n3
    if n3<0:
        print("(Ingrese un numero entero positivo)")
    else:
        nCuadrada=sqrt(n3)
        return calcular_raiz_cuadrada(nCuadrada)

def calcular_raiz_cuadrada(nCuadrada):
    res=nn3%2
    if res==1:
        r=int(nCuadrada)
        return r
    return int(nCuadrada)

def convertir_a_decimal(n4,index=0,n=0):
    romanos={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    if index!=len(n4):
        if index>0 and romanos[n4[index]]>romanos[n4[index-1]]:
            n+=(romanos[n4[index]]-(2*romanos[n4[index-1]]))
            convertir_a_decimal(n4,index+1,n)
        else:
            n+=romanos[n4[index]]
            convertir_a_decimal(n4,index+1,n)
    print(n)
    return convertir_a_decimal(n+1)

def sumar_numeros_enteros(n5,index,n=0):
    if index!=len(n5):
        n+=int(n5[index])
        #print(n)
        sumar_numeros_enteros(n5,index+1,n)
    else:
        print(n)
        return n
    

while True:
    print("")
    print("|---------------------------------------|")
    print("|          FUNCIONES RECURSIVAS         |")
    print("|---------------------------------------|")
    print("|  1) Convertir a Binario               |")
    print("|  2) Contar Digitos                    |")
    print("|  3) Raiz Cuadrada Entera              |")
    print("|  4) Convertir a Decimal desde Romano  |")
    print("|  5) Suma de Numeros Enteras           |")
    print("|  0) Salir                             |")
    print("|---------------------------------------|")
    print("")

    try:
        n=int(input("Ingrese una Opcion: "))
        if n==1:
            print("")
            print("|---------------------------------------|")
            print("|          Convertir a Binario          |")
            print("|---------------------------------------|")
            print("")
            n1=int(input("  Ingrese un numero:"))
            print("")
            print("  El numero ",n1," en binario es: ",convertir_a_binario(n1))
            print("")
            print("  Presione cualquier tecla para continuar...")
            msvcrt.getch()
        elif n==2:
            print("")
            print("|---------------------------------------|")
            print("|             Contar Digitos            |")
            print("|---------------------------------------|")
            print("")
            n2=int(input("  Ingrese un numero:"))
            print("")
            print("  El numero ",n2," tiene ",contar_digitos(n2)," digitos.")
            print("")
            print("  Presione cualquier tecla para continuar...")
            msvcrt.getch()
        elif n==3:
            print("")
            print("|---------------------------------------|")
            print("|          Raiz Cuadrada Entera         |")
            print("|---------------------------------------|")
            print("")
            n3=int(input("  Ingrese un numero:"))
            print("")
            print("  La raiz cuadrada entera de ",n3," es ",raiz_cuadrada_entera(n3))
            print("")
            print("  Presione cualquier tecla para continuar...")
            msvcrt.getch()
        elif n==4:
            print("")
            print("|---------------------------------------|")
            print("|    Convertir a Deciaml desde Romano   |")
            print("|---------------------------------------|")
            print("")
            n4=input("  Ingrese un numeroen Romano:")
            print("")
            print("El numero Romano ingresado es igual a: ")
            convertir_a_decimal(n4)
            print("")
            print("  Presione cualquier tecla para continuar...")
            msvcrt.getch()
        elif n==5:
            print("")
            print("|---------------------------------------|")
            print("|          Sumar Numeros Enteros        |")
            print("|---------------------------------------|")
            print("")
            n5=input("  Ingrese los nueros:")
            print("")
            print("La suma de los numeros es de : ")
            sumar_numeros_enteros(n5,0)
            print("")
            print("  Presione cualquier tecla para continuar...")
            msvcrt.getch()
        elif n==0:
            break
        else:
            print("")
            print("Opcion no valida")
            print("Presione cualquier tecla para continuar...")
            msvcrt.getch()
    except:
        print()
        print("Ingrese un numero del menu")
        print("Presione cualquier tecla para continuar...")
        msvcrt.getch()