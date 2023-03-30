#6. Retomamos el código visto en la teoría, que informaba si una palabra contenía la letra *a* en una palabra ingresada
#Si ahora queremos saber si contiene la letra *a* y también la letra *n*, cómo lo modificamos?

palabra = input("Ingresá una palabra: ")
if "a" in palabra and "n" in palabra:
    print("Hay letras a y n.")
else:
    print("No hay letras a y n. ")