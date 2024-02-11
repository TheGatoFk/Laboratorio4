from collections import deque
import time

while True:
    print("\n\n\t\tMenu Principal\n")
    print(" 1. Implementacion de pila.\n",
          "2. Implementacion de una cola usando lista.\n",
          "3. Verificacion de parentesis.\n",
          "4. Implementacion de una cola con dos pilas.\n",
          "5. Revertir la mitad de una cola.\n",
          "6. Salir de menu.")

    opc = input("\nIngrese una opcion: ")

    if opc.isdigit():
        opc = int(opc)
        
        if opc==1:
            print("\n\t<<<<<< Implementacion de pila >>>>>>\n")

            #Funcion para añadir elemento en la pila.
            def push(pila,elemento):
                pila.append(elemento)

            #Funcion para eliminar elemento de la pila.
            def pop(pila):
                eliminado=pila.pop()
                return eliminado

            #Funcion para ver el elemento superior.
            def peek(pila):
                return pila[-1]
            
            #Funcion para invertir la pila.
            def pila_invertida(pila):
                return pila.reverse()
                                    
            #Creacion de una pila usando lista.
            marca=["toyota","honda","mazda"]
            print("Pila original:")
            print(marca,"\n")

            #Añadir elemento en la pila.
            push(marca,"subaru")
            print(f"Añadiendo elemento: {marca[-1]}")
            print(marca,"\n")

            #Eliminar elemento de la pila.
            eliminar=pop(marca)
            print(f"Elemento eliminado: {eliminar}")
            print(marca,"\n")

            #Ver elemento superior.
            elemento_superior=peek(marca)
            print(f"El elemento superior es: {elemento_superior}\n")

            #Invertir orden de lista.
            ver_pila_invertida=pila_invertida(marca)
            print("pila invertida:")
            print(marca,"\n")
            break
        
        elif opc==2:
            print("\n\t<<<<<< Implementacion de una cola usando lista. >>>>>>\n")

            #Funcion para agregar elemento a la cola.
            def enqueue(cola,elemento):
                cola.appendleft(elemento)

            #Funcion para eliminar elemento de la cola.
            def dequeue(cola):
                cola.popleft()

            #Funcion para ver el primer elemento de la cola.
            def front(cola):
                return cola[0]

            #Creacion de una cola.
            letras=deque("bcdefg")
            print("Cola original:")
            print(letras,"\n")

            #Añadiendo elemento en la cola.
            añadir=enqueue(letras,'a')
            print(f"letra añadida: {letras[0]}")
            print(letras,"\n")

            #Eliminando elemento de la cola.
            print(f"Letra eliminada: {letras[0]}")
            elimnar=dequeue(letras)
            print(letras,"\n")

            #Ver el primer elemento de la cola.
            primer_elemento=front(letras)
            print(f"La primera letra es: {primer_elemento}")
            print(letras,"\n")

            #Función para agregar mesa a la cola.
            def agregar_mesa(cola_mesa, mesa):
                cola_mesa.append(mesa)

            #Función para eliminar y devolver la primera mesa de la cola.
            def atender_mesa(cola_mesa):
                return cola_mesa.popleft()

            #Función para ver la primera mesa de la cola.
            def primera_mesa(cola_mesa):
                return cola_mesa[0] if cola_mesa else None  # Manejo de cola vacía

            #Función para simular la atención de mesas.
            def simulacion_atencion(cola_mesa):
                print("Simulación de atención en una fila:")
                while cola_mesa:
                    mesa_actual = atender_mesa(cola_mesa)
                    print(f"Atendiendo a la mesa: {mesa_actual}")
                    time.sleep(1)  # Simulación de tiempo de atención
                    print("Mesa atendida.\n")
                    time.sleep(0.5)  # Espera antes de atender a la siguiente mesa
                print("No hay más mesas en la fila.")

            #Creación de una cola de mesas.
            cola_mesa = deque(["mesa 1", "mesa 2", "mesa 3", "mesa 4", "mesa 5"])

            #Ejecutar la simulación de atención de mesas.
            simulacion_atencion(cola_mesa)
            break

        elif opc==3:
            print("\n\t<<<<<< Verificacion de parentesis >>>>>>\n")

            #Funcion para verificar lso parentesis.
            def verificar_parentesis(parentesis):
                pila = []
                for caracter in parentesis:
                    if caracter == '(':
                        pila.append(caracter)
                    elif caracter == ')':
                        if not pila:
                            return False  
                        pila.pop()  
                return len(pila) == 0  

            parentesis1 = "((()))"
            parentesis2 = "()()()"
            parentesis3 = "(()))"

            print("Parentesis1: () () ()")
            print(verificar_parentesis(parentesis2),"\n")

            print("Parentesis2: ( ( () ) )")
            print(verificar_parentesis(parentesis1),"\n")

            print("Parentesis3: ( () ) )")
            print(verificar_parentesis(parentesis3),"\n") 
            break
        
        elif opc==4:
            print("\n\t<<<<<< Implementacion de una cola con dos pilas >>>>>>\n")

            #Creando una clase llamada colaconPilas.
            class ColaConPilas:
                def __init__(self):
                    self.entrada = []
                    self.salida = []

                #Funcion para añadir elementos.
                def añadir_elemento(self, elemento):
                    self.entrada.append(elemento)
                
                #Funcion para eliminar elementos
                def eliminar_elemento(self):
                    if not self.salida:
                        if not self.entrada:
                            return None  #La cola esta vacia.
                        #Transferir elementos de entrada a salida.
                        while self.entrada:
                            self.salida.append(self.entrada.pop())
                    return self.salida.pop()

            cola = ColaConPilas()
            cola.añadir_elemento(1)
            cola.añadir_elemento(2)
            cola.añadir_elemento(3)
            print(cola.eliminar_elemento()) 
            print(cola.eliminar_elemento()) 
            cola.añadir_elemento(4)
            print(cola.eliminar_elemento()) 
            print(cola.eliminar_elemento()) 
            print(cola.eliminar_elemento()) 
            break
        
        elif opc==5:
            print("\n\t<<<<<< Revertir la mitad de una cola >>>>>>\n")

            #Funcion para revertir la mitad de la cola.
            def revertir_mitad_cola(cola):
                pila = []
                largo_cola = len(cola)
                mitad = largo_cola // 2

                #Añadir la mitad de los elementos de la cola a la pila.
                for _ in range(mitad):
                    pila.append(cola.popleft())

                #Revertir la mitad de la cola usando la pila.
                for _ in range(mitad):
                    cola.appendleft(pila.pop())

                #Si la cola tenía un número impar de elementos, mover el elemento del centro al final.
                if largo_cola % 2 != 0:
                    cola.append(cola.popleft())

            #Crear una cola
            cola_original = deque([1,2,3,4,5])

            #Mostrar la cola original
            print("Cola Original:", cola_original)

            #Invertir la mitad de la cola
            revertir_mitad_cola(cola_original)

            #Mostrar la cola invertida
            print("Cola Invertida:", cola_original)

            break

        elif opc==6:
            print("Saliendo el menu...")
            break

        else:
            print("Opcion incorrecta, ingreso una valor fuera del rango establecido.\n")
    else:
        print("OOpcion incorrecta, ingreso un caracter.\n")
