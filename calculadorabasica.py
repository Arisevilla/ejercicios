def calculadora():

      while True:
            print("Calculadora")

            numero1=float(input("Ingresa el primer número de la operación: "))
            numero2=float(input("Ingresa el segundo número de la operación: "))
            print("""
             Menú de opciones:
             1- Sumar
             2- Restar
             3- Multiplicar
             4- Dividir     
             5- Apagar calculadora
             """)
            operacion =  int(input("Ingresa el número de la operación a realizar: "))
            if operacion== 1:
                  print(numero1 + numero2)
            elif operacion== 2:
                   print(numero1 - numero2)
            elif operacion== 3:
                  print(numero1 * numero2)
            elif operacion== 4:
                  print(numero1 / numero2)
            elif operacion== 5:
                  break
            else:
                  print("Opcion incorrecta")

resultado=calculadora()
