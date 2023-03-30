#4. Para la aceptación de un artículo en un congreso se definen las siguientes especificaciones que deben cumplir y recomendaciones de escritura:
#* **título**: 10 palabras como máximo
#* cada oración del **resumen**:
#    * hasta 12 palabras: fácil de leer                 1
#    * entre 13-17 palabras:  aceptable para leer       2       2
#    * entre 18-25 palabras: difícil de leer            1       1
#    * mas de 25 palabras: muy difícil                  2       2

from collections import Counter
evaluar = """título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python 
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources provides the promise of capturing unprecedented details of large-scale complex systems. However, the specialized knowledge required for developing such ABMs creates barriers to wider adoption and utilization. Here we present our experiences in developing an initial implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our experiences in developing ABM toolkits, including Repast for High Performance Computing (Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling system that can exploit the largest HPC resources and emerging computing architectures."""

evaluar = evaluar.split("\n")

title= evaluar[0].replace("título: ", "").split()
summary = evaluar [1].replace("resumen: ", "").split(". ")

sentences = {'facil': 0, 'aceptable': 0, 'dificil': 0, 'muyDificil': 0}

for i in summary:
    match len(i.split()):
        case lenght if 0 < lenght < 13: sentences['facil']+=1
        case lenght if 12 < lenght < 18: sentences['aceptable']+=1
        case lenght if 17 < lenght < 26: sentences['dificil']+=1
        case lenght if 25 < lenght : sentences['muyDificil']+=1

if len(title) == 10:
    print ("titulo: ok")
else:
    print ("titulo: no")

print (f"Cantidad de oraciones fáciles de leer: {sentences['facil']}, aceptables para leer: {sentences['aceptable']}, dificil de leer: {sentences['dificil']},  muy difícil de leer:{sentences['muyDificil']}")