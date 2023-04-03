#7. Dada una frase identificar mayúsculas, minúsculas y caracteres no letras y contar la cantidad de palabras sin distinguir entre mayúsculas y minúsculas, en la frase. 
from collections import Counter
import string
texto = """
 El salario promedio de un hombre en Argentina es de $60.000, mientras que el de una mujer es de $45.000. Además, las mujeres tienen menos posibilidades de acceder a puestos de liderazgo en las empresas.
  """
resul={'mayus':0,'minus':0,'noLetra':0}                                    #identificar mayus minus y caracteres no letras
for i in texto:
    match i:
        case i if i in string.ascii_lowercase:
            resul['minus']+=1
        case i if i in string.ascii_uppercase:
            resul['mayus']+=1
        case _:
            resul['noLetra']+=1

texto = texto.lower().split()
textLen = list(filter(lambda x: x[0] in string.ascii_letters, texto))       #cantidad de palabras en la frase

cantWords = Counter(texto)                                                  #cantidad de veces que se repite cada palabra

print (cantWords)
print (resul)
print (len(textLen))
