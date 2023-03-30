#3. Dado el siguiente texto guardado en la varible jupyter_info
# solicite por teclado una letra e imprima las palabras que comienzan con dicha letra.
# En caso que no se haya inrgesado un letra, indique el error. 


import string

jupyter_info = """ JupyterLab is a web-based interactive development
environment for Jupyter notebooks,
code, and data. JupyterLab is flexible: configure and arrange the user
interface to support a wide range
of workflows in data science, scientific computing, and machine learning.
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing
ones.
"""

print (" ","-"*90)
character =  input("Palabra a buscar con: ")

print (" ","-"*90)

match = False

while not (character in string.ascii_letters):                                                      
    character =  input("La letra ingresada no es un caracter, por favor intente nuevamente: ")

for i in jupyter_info.split():                                                                      
    if i.lower().startswith(character.lower()):
        print (i, end=" ")
        match = True
if not match:
    print ("No se encontro una palabra que empiece por esa letra")
print ("\n","-"*90)