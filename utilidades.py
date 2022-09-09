""" Módulo para cálculos diversos """

def precio_con_descuento(precio_original, descuento):
    """Calcula y retorna el precio con descuento."""
    nuevo_precio = (100 - descuento) * precio_original / 100
    return nuevo_precio

def suma_lista(lista_de_numeros):
    resultado = 0
    for numero in lista_de_numeros:
        resultado += numero
    return resultado

