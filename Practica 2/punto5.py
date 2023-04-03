#5. Dada una frase y un string ingresados por teclado (en ese orden), genere una lista de palabras, y sobre ella, informe la cantidad de palabras en las que se encuentra el string
# . No distingir entre mayúsculas y minúsculas.
#
#**Ejemplo 1**
#- **Para la frase**: "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres."
#- **Palabra**: "tres"
#- **Resultado**: 3


from collections import Counter

phrase = input('Ingresar frase: ')
word = input ('Ingresar palabra: ')

phraseSplit = phrase.lower().replace(".", "").replace(",", "").split()

cant = Counter(phraseSplit)

print(f"Para la frase: {phrase}")
print(f"Palabra: {word}")
print(f"Resultado: {cant[word.lower()]}")

