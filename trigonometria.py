# --- F U E N T E S ---
#https://www.matesfacil.com/ESO/geometria_plana/trigonometria/problemas-resueltos-trigonometria-secundaria-seno-coseno-triangulo-angulo.html
# --- F U E N T E S ---

#...IMPORTAR LIBRERIAS Y DEFINIR CONSTANTES...
import time
import math

pi = math.pi
lados = []
angulos = []
#...IMPORTAR LIBRERIAS Y DEFINIR CONSTANTES...

#...DEFINIR FUNCIONES TRIGONOMETRICAS...
def sin(grados):
    return math.sin(math.radians(grados))
def cos(grados):
    return math.cos(math.radians(grados))
def tan(grados):
    return math.tan(math.radians(grados))
def asin(grados):
    return math.degrees(math.asin(grados))
def acos(grados):
    return math.degrees(math.acos(grados))
def atan(grados):
    return math.degrees(math.atan(grados))
#...DEFINIR FUNCIONES TRIGONOMETRICAS...



# --- FUNCIONES ---

#...Funcion para el triangulo rectangulo...

def hallar_angulos(A, B, C, a, b, c):

    valores = [A, B, C, a, b, c]

    print("\n--- PROCESO ---\n")

    #--- HALLAR LOS ANGULOS ---

    #.....lado a
    if a == 0 and A != 0 and B != 0:
        a = atan((A / B))
        a = round(a,3)
        print(f"a = atan(({A} / {B}))")
        print(f"a = atan(({A / B}))")
        print("a = ",a)
        print("\n")
    if a == 0 and A != 0 and C != 0:
        a = asin((A / C))
        a = round(a,3)
        print(f"a = asin(({A} / {C}))")
        print(f"a = asin(({A / C}))")
        print("a = ",a)
        print("\n")
    if a == 0 and B != 0 and C != 0:
        a = acos((B / C))
        a = round(a,3)
        print(f"a = acos(({B} / {C}))")
        print(f"a = acos(({B / C}))")
        print("a = ",a)
        print("\n")
    #.....lado b
    if b == 0 and A != 0 and B != 0:
        b = atan((B / A))
        b = round(b,3)
        print(f"b = atan(({B} / {A}))")
        print(f"b = atan(({B / A}))")
        print("b = ",b)
        print("\n")
    if b == 0 and A != 0 and C != 0:
        b = acos((A / C))
        b = round(b,3)
        print(f"b = acos(({A} / {C}))")
        print(f"b = acos(({A / C}))")
        print("b = ",b)
        print("\n")
    if b == 0 and B != 0 and C != 0:
        b = asin((B / C))
        b = round(b,3)
        print(f"b = asin(({B} / {C}))")
        print(f"b = asin(({B / C}))")
        print("b = ",b)
        print("\n")
    if c == 0:
        c = 180 - (a+b)
    #....hallar los angulos...

    print("--- PROCESO ---\n")

    solucion = f"""
    ... Solucion ...
    Lado A = {round(A,3)}
    Lado B = {round(B,3)}
    Lado C = {round(C,3)}
    
    angulo a = {round(a,3)}°
    angulo b = {round(b,3)}°
    angulo c = {round(c,3)}°
    ... Solucion ...
    """
    return solucion

def hallar_lados(A, B, C, a, b, c):
    valores = [A, B, C, a, b, c]
    print("\n--- PROCESO ---\n")
    while True:

        # --- HALLAR C ---
        if A != 0 and B != 0 and C == 0:    #...Teorema de Pitagoras...
            print("h = √(", A, "² + ", B,"²)")
            suma = (A ** 2) + (B ** 2)
            print("h = √(",suma,")")
            C = (suma ** 0.5)
            C = round(C, 3)
            print("h = (",C,")")
            valores[2] = C
            print("\n")
        if C == 0 and A != 0 and a != 0:    #...Caso 1....Hallar hipotenusa
            C = (A / sin(a))
            valores[2] = C
            print("C = ", A, "/ sin(",a,")")
            print("C = ", A, "/ ",sin(a))
            print(C)
            print("\n")
        if C == 0 and B != 0 and b != 0:    #...Caso 2....Hallar hipotenusa
            C = (B / sin(b))
            valores[2] = C
            print("C = ", B, "/ sin(",b,")")
            print("C = ", B, "/ ",sin(b))
            print(C)
            print("\n")
        
        # --- HALLAR A ---
        if A == 0 and a != 0 and B != 0:    #...Caso 1....Cateto adyacente
            C = (B / cos(a))
            A = (C * sin(a))
            valores[0] = A
            valores[2] = C
            print("C = ", B, "/ cos(",a,")")
            print("C = ", B, "/ ",cos(a))
            print(C)
            print("A = ", C, "/ sin(",a,")")
            print("A = ", C, "/ ",sin(a))
            print(A)
            print("\n")
        if A == 0 and C != 0 and b != 0:    #...Caso 2....Angulo adyacente y Hipotenusa
            A = (C * (cos(b)))
            valores[0] = A
            print("A = ", C, "* cos(",b,")")
            print("A = ", C, "* ", cos(b))
            print("A = ", A)
            print("\n")
        if A == 0 and C != 0 and a != 0:    #...Caso 3....Angulo opuesto y Hipotenusa
            A = (C * (sin(a)))
            valores[0] = A
            print("A = ", C, "* sin(",a,")")
            print("A = ", C, "* ", sin(a))
            print("A = ", A)
            print("\n")
        # --- HALLAR A ---

        # --- HALLAR LADO B ---
        if B == 0 and b != 0 and A != 0:    #...Caso 1....Cateto adyacente
            C = (A / cos(b))
            B = (C * sin(b))
            valores[1] = B
            valores[2] = C
            print("C = ", A, "/ cos(",b,")")
            print("C = ", A, "/ ", cos(b))
            print(C)
            print("B = ", C, "/ sin(",b,")")
            print("B = ", C, "/ ", sin(b))
            print(B)
            print("\n")
        if B == 0 and C != 0 and a != 0:    #...Caso 2....Angulo adyacente y Hipotenusa
            B = (C * (cos(a)))
            valores[1] = B
            print("B = ", C, "* cos(",b,")")
            print("B = ", C, "* ", cos(c))
            print("B = ", B)
            print("\n")
        if B == 0 and C != 0 and b != 0:    #...Caso 3....Angulo opuesto y Hipotenusa
            B = (C * (sin(b)))
            valores[1] = B
            print("B = ", C, "* sin(",b,")")
            print("B = ", C, "* ", sin(b))
            print("B = ", B)
            print("\n")
        # --- HALLAR LADO B ---

        #...Verificador...
        if A != 0 and B != 0 and C != 0:
            break

    print("--- PROCESO ---\n")

    solucion = f"""
    ... Solucion ...
    Lado A = {round(A,3)}
    Lado B = {round(B,3)}
    Lado C = {round(C,3)}
    
    angulo a = {round(a,3)}°
    angulo b = {round(b,3)}°
    angulo c = {round(c,3)}°
    ... Solucion ...
    """
    return solucion

def todo(A, B, C, a, b, c):
    valores = [A, B, C, a, b, c]
    print("\n--- PROCESO ---\n")
    while True:

        # --- HALLAR C ---
        if C == 0 and A != 0 and B != 0:    #...Teorema de Pitagoras...
            print("h = √(", A, "² + ", B,"²)")
            suma = (A ** 2) + (B ** 2)
            print("h = √(",suma,")")
            C = (suma ** 0.5)
            C = round(C, 3)
            print("h = (",C,")")
            valores[2] = C
            print("\n")
        if C == 0 and A != 0 and a != 0:    #...Caso 1....Hallar hipotenusa
            C = (A / sin(a))
            valores[2] = C
            print("C = ", A, "/ sin(",a,")")
            print("C = ", A, "/ ",sin(a))
            print(C)
            print("\n")
        if C == 0 and B != 0 and b != 0:    #...Caso 2....Hallar hipotenusa
            C = (B / sin(b))
            valores[2] = C
            print("C = ", B, "/ sin(",b,")")
            print("C = ", B, "/ ",sin(b))
            print(C)
            print("\n")
        
        # --- HALLAR A ---
        if A == 0 and a != 0 and B != 0:    #...Caso 1....Cateto adyacente
            C = (B / cos(a))
            A = (C * sin(a))
            valores[0] = A
            valores[2] = C
            print("C = ", B, "/ cos(",a,")")
            print("C = ", B, "/ ",cos(a))
            print(C)
            print("A = ", C, "/ sin(",a,")")
            print("A = ", C, "/ ",sin(a))
            print(A)
            print("\n")
        if A == 0 and C != 0 and b != 0:    #...Caso 2....Angulo adyacente y Hipotenusa
            A = (C * (cos(b)))
            valores[0] = A
            print("A = ", C, "* cos(",b,")")
            print("A = ", C, "* ", cos(b))
            print("A = ", A)
            print("\n")
        if A == 0 and C != 0 and a != 0:    #...Caso 3....Angulo opuesto y Hipotenusa
            A = (C * (sin(a)))
            valores[0] = A
            print("A = ", C, "* sin(",a,")")
            print("A = ", C, "* ", sin(a))
            print("A = ", A)
            print("\n")
        # --- HALLAR A ---

        # --- HALLAR LADO B ---
        if B == 0 and b != 0 and A != 0:    #...Caso 1....Cateto adyacente
            C = (A / cos(b))
            B = (C * sin(b))
            valores[1] = B
            valores[2] = C
            print("C = ", A, "/ cos(",b,")")
            print("C = ", A, "/ ", cos(b))
            print(C)
            print("B = ", C, "/ sin(",b,")")
            print("B = ", C, "/ ", sin(b))
            print(B)
            print("\n")
        if B == 0 and C != 0 and a != 0:    #...Caso 2....Angulo adyacente y Hipotenusa
            B = (C * (cos(a)))
            valores[1] = B
            print("B = ", C, "* cos(",b,")")
            print("B = ", C, "* ", cos(c))
            print("B = ", B)
            print("\n")
        if B == 0 and C != 0 and b != 0:    #...Caso 3....Angulo opuesto y Hipotenusa
            B = (C * (sin(b)))
            valores[1] = B
            print("B = ", C, "* sin(",b,")")
            print("B = ", C, "* ", sin(b))
            print("B = ", B)
            print("\n")
        # --- HALLAR LADO B ---

        #...Verificador...
        if A != 0 and B != 0 and C != 0:
            break
    
    #....hallar los angulos...
    if a == 0 and A != 0 and B != 0:
        a = atan((A / B))
        a = round(a,3)
        print(f"a = atan(({A} / {B}))")
        print(f"a = atan(({A / B}))")
        print("a = ",a)
        print("\n")
    if a == 0 and A != 0 and C != 0:
        a = asin((A / C))
        a = round(a,3)
        print(f"a = asin(({A} / {C}))")
        print(f"a = asin(({A / C}))")
        print("a = ",a)
        print("\n")
    if a == 0 and B != 0 and C != 0:
        a = acos((B / C))
        a = round(a,3)
        print(f"a = acos(({B} / {C}))")
        print(f"a = acos(({B / C}))")
        print("a = ",a)
        print("\n")
    #.....lado b
    if b == 0 and A != 0 and B != 0:
        b = atan((B / A))
        b = round(b,3)
        print(f"b = atan(({B} / {A}))")
        print(f"b = atan(({B / A}))")
        print("b = ",b)
        print("\n")
    if b == 0 and A != 0 and C != 0:
        b = acos((A / C))
        b = round(b,3)
        print(f"b = acos(({A} / {C}))")
        print(f"b = acos(({A / C}))")
        print("b = ",b)
        print("\n")
    if b == 0 and B != 0 and C != 0:
        b = asin((B / C))
        b = round(b,3)
        print(f"b = asin(({B} / {C}))")
        print(f"b = asin(({B / C}))")
        print("b = ",b)
        print("\n")
    if c == 0:
        c = 180 - (a+b)
    #....hallar los angulos...

    print("--- PROCESO ---\n")

    solucion = f"""
    ... Solucion ...
    Lado A = {round(A,3)}
    Lado B = {round(B,3)}
    Lado C = {round(C,3)}
    
    angulo a = {round(a,3)}°
    angulo b = {round(b,3)}°
    angulo c = {round(c,3)}°
    ... Solucion ...
    """
    return solucion

#...Funcion beta para casos especiales doble triangulo...
#a, B, b, h, , x
def especial(alfa, beta, B):            
        h = (((-(B)) * (tan(beta))) / (1 - ((tan(beta)) / (tan(alfa)))))
        solucion = round(h,3)
        return solucion
#...Funcion beta para casos especiales doble triangulo...

# --- FUNCIONES ---
while True:
    lados = []
    angulos = []

    #...INICIO DEL PROGRAMA...
    print("\n.....CARGANDO PROGRAMA TRIGONOMETRIA.....")
    #time.sleep(1)
    #...INICIO DEL PROGRAMA...


    # --- TRIANGULO ---
    print("\n--- Triangulo ---")
    print("""                             
                                        *
                                    *   *
                 h              *  "b"  *
                            *           *
                        *               *   A
                    *                   *
                *   "a"            "c"  *             
            *   *   *   *   *   *   *   *
                        B
    """)
    print("----------------")
    # --- TRIANGULO ---


    print("""
... Opciones ...
1- Hallar lados
2- Hallar Angulos
3- Todo
""")
    
    opcion = int(input("> "))

    if opcion == 1:
        variable = float(input("> Ingrese el valor del lado A = "))     #...index 0 for A
        lados.append(variable)
        variable = float(input("> Ingrese el valor del lado B = "))     #...index 1 for B
        lados.append(variable)
        variable = float(input("> Ingrese el valor del lado C = "))     #...index 2 for C
        lados.append(variable)
        print(" ")
        variable = float(input("> Ingrese el valor del angulo a = "))     #...index 3 for A
        angulos.append(variable)
        variable = float(input("> Ingrese el valor del angulo b = "))     #...index 4 for B
        angulos.append(variable)
        variable = float(input("> Ingrese el valor del angulo c = "))     #...index 5 for C
        angulos.append(variable)
        respuesta = hallar_lados(lados[0], lados[1], lados[2], angulos[0],  angulos[1],  angulos[2])
        print(respuesta)
        
    elif opcion == 2:
        variable = float(input("> Ingrese el valor del lado A = "))     #...index 0 for A
        lados.append(variable)
        variable = float(input("> Ingrese el valor del lado B = "))     #...index 1 for B
        lados.append(variable)
        variable = float(input("> Ingrese el valor del lado C = "))     #...index 2 for C
        lados.append(variable)
        print(" ")
        variable = float(input("> Ingrese el valor del angulo a = "))     #...index 3 for A
        angulos.append(variable)
        variable = float(input("> Ingrese el valor del angulo b = "))     #...index 4 for B
        angulos.append(variable)
        variable = float(input("> Ingrese el valor del angulo c = "))     #...index 5 for C
        angulos.append(variable)
        respuesta = hallar_angulos(lados[0], lados[1], lados[2], angulos[0],  angulos[1],  angulos[2])
        print(respuesta)

    elif opcion == 3:
        variable = float(input("> Ingrese el valor del lado A = "))     #...index 0 for A
        lados.append(variable)
        variable = float(input("> Ingrese el valor del lado B = "))     #...index 1 for B
        lados.append(variable)
        variable = float(input("> Ingrese el valor del lado C = "))     #...index 2 for C
        lados.append(variable)
        print(" ")
        variable = float(input("> Ingrese el valor del angulo a = "))     #...index 3 for A
        angulos.append(variable)
        variable = float(input("> Ingrese el valor del angulo b = "))     #...index 4 for B
        angulos.append(variable)
        variable = float(input("> Ingrese el valor del angulo c = "))     #...index 5 for C
        angulos.append(variable)
        respuesta = todo(lados[0], lados[1], lados[2], angulos[0],  angulos[1],  angulos[2])
        print(respuesta)
    else:
        print("ERROR")

        exit

#...OPCIONES...    
    print("Desea hacer otro calculo?\nResponda ""s"" para si o ""n"" para no")
    opcion = str(input(" > "))
    opcion = opcion.lower()
    if opcion == "s":
        continue
    elif opcion == "n":
        print("\n--- Fin del programa: Creado por Juan Carlos Largo ---")
        
        exit()
    else:
        print("ERROR")
        
        exit()
#...OPCIONES...