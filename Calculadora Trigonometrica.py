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
def triangulo_rectangulo(A, B, C, a, b, c):
    valores = [A, B, C, a, b, c]
    while True:
        #...Pitagoras
        if A != 0 and B != 0:
            print("\n")
            print("h = raiz(", A, "* + ", B,"*)")
            suma = (A ** 2) + (B ** 2)
            print("h = raiz(",suma,")")
            C = (suma ** 0.5)
            C = round(C, 3)
            print("h = (",C,")")
            valores[2] = C
        #...Caso 1....Hallar hipotenusa
        if C == 0 and A != 0 and a != 0:
            C = (A / sin(a))
            valores[2] = C
        if C == 0 and B != 0 and b != 0:
            C = (B / sin(b))
            valores[2] = C
        #...Caso 2....Cateto adyacente
        if A == 0 and a != 0 and B != 0:
            C = (B / cos(a))
            A = (C * sin(a))
            valores[0] = A
            valores[2] = C
        if B == 0 and b != 0 and A != 0:
            C = (A / cos(b))
            B = (C * sin(b))
            valores[1] = B
            valores[2] = C
        #...Caso 3....Lado y Hipotenusa
        if A == 0 and B != 0 and C != 0:
            A = (C ** 2) - (B ** 2)
            A = (A ** 0.5)
            valores[0] = A
        if B == 0 and A != 0 and C != 0:
            B = (C ** 2) - (A ** 2)
            B = (B ** 0.5)
            valores[1] = B
        #...Caso 4....Angulo y Hipotenusa
        if A == 0 and C != 0 and a != 0:
            A = (C * (sin(a)))
            valores[0] = A
        if B == 0 and C != 0 and b != 0:
            B = (C * (sin(b)))
            valores[1] = B
        #...Verificador
        if A != 0 and B != 0 and C != 0:
            break
    if a == 0:
        a = asin((A / C))
        a = round(a,3)
    if b == 0:
        b = asin((B / C))
        a = round(a,3)
    if c == 0:
        c = 90
    solucion = f"""
    A = {round(A,3)}
    B = {round(B,3)}
    C = {round(C,3)}
    
    a = {round(a,3)}
    b = {round(b,3)}
    c = {round(c,3)} 
    """
    return solucion
#...FUNCIONES...

#...Funcion para casos especiales doble triangulo...
#a, B, b, h, , x
def especial(alfa, beta, B):            
        h = (((-(B)) * (tan(beta))) / (1 - ((tan(beta)) / (tan(alfa)))))
        solucion = round(h,3)
        return solucion
#...Funcion para casos especiales doble triangulo...





# --- FUNCIONES ---


#...INICIO DEL PROGRAMA...
print("\n.....CARGANDO PROGRAMA TRIGONOMETRIA.....")
time.sleep(1)
print("--- Creado Por JuanCarlosLB ---")
#...INICIO DEL PROGRAMA...


# --- TRIANGULO ---
print("\n--- Triangulo ---")
print("""                             
                                *
                            *   *
             h          *  "b"  *
                    *           *
                *               *   A
            *  "a"         "c"  *
        *   *   *   *   *   *   *
                    B
""")
print("----------------")
# --- TRIANGULO ---

print(
"""
--- Opciones ---
1- Normal
2- Triangulos Unidos
"""
)
opcion = int(input("> "))


#...OPCIONES...
if opcion == 1:
    variable = float(input("> Ingrese el valor de A = "))     #...index 0 for A
    lados.append(variable)
    variable = float(input("> Ingrese el valor de B = "))     #...index 1 for B
    lados.append(variable)
    variable = float(input("> Ingrese el valor de C = "))     #...index 2 for C
    lados.append(variable)
    print(" ")
    variable = float(input("> Ingrese el valor de a = "))     #...index 3 for A
    angulos.append(variable)
    variable = float(input("> Ingrese el valor de b = "))     #...index 4 for B
    angulos.append(variable)
    variable = float(input("> Ingrese el valor de c = "))     #...index 5 for C
    angulos.append(variable)
    respuesta = triangulo_rectangulo(lados[0], lados[1], lados[2], angulos[0],  angulos[1],  angulos[2])
    print(respuesta)