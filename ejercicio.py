print()

c = False

while True:
    try:
        v1 = int(input("Ingresa solo un numero entero: "))
        v2 = int(input("Ingresa otro numero entero: "))

        print(v1 / v2)
    
        c = True

        break
    
    except ValueError:
        print("Solo se aceptan numeros enteros..")
    
    except ZeroDivisionError:
        print("No se puede dividir por cero....")
        
    else:
        print("HOLA")
        print()
    
    finally:
        if c == True:
            print("Finalizando programa")
        else:
            print("Intenta nuevamente........")
    
    