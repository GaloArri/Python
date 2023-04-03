#8. Escriba un programa que solicite que se ingrese una palabra o frase y permita identificar si la misma es un Heterograma
#  Un Heterograma es una palabra o frase que no tiene ninguna letra repetida entre sus caracteres.
#
#**Tener en cuenta**
#- Lo que no se puede repetir en la frase son sólo aquellos caracteres que sean letras.
#- No se distingue entre mayúsculas y minúsculas, es decir si en la frase o palabra tenemos la letra "T" y la letra "t" la misma NO será un Hererograma.
#- Para simplificar el ejercicio vamos a tomar como que las letras con tilde y sin tilde son distintas. Ya que Python las diferencia

from  collections import Counter
text=input("Ingrese una palabra o frase: ")

text = text.replace(" ", "").lower()

count = Counter(text)

first = list(Counter(count).most_common())

if (first[0][1] > 1):
    print ("no")
else:
    print ("si")
