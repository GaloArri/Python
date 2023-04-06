nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David', 'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge', 'JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

#1. Generar una estructura con todas las notas relacionando el nombre del estudiante con las notas. Utilizar esta estructura para la resol

def nombre_con_notas(nombres, notas_1, notas_2):                                        #genero un diccionario con una lista que contenga las dos notas de ese alumno
    nombres_list = nombres.replace("'","").replace(",","").split()                      #genero una lista con los nombres por separado, quitando las comas y las comillas simples
    alumnos_notas = {}                                                  
    aux=0                                                                               #uso un auxiliar para iterar la lista ya que el for no me devuelve un int
    for i in nombres_list:
        alumnos_notas[i] = [notas_1[aux],notas_2[aux]]                                  #guardo el nombre del alumno y sus notas
        aux+=1                                                                          #aumento el iterador
    return alumnos_notas   
 
alumnos_con_notas = nombre_con_notas(nombres, notas_1, notas_2)
print (alumnos_con_notas)

print ("="*90)

# 2. Calcular el promedio de notas de cada estudiante.

def promedio_alumno (alumnos_con_notas):                                                #genero un diccionario con los nombres y el promedio de cada alumno
    alumnos_promedio = {}
    for i in alumnos_con_notas.keys():                                                  #recorro mediante las keys el diccionario con las notas
        alumnos_promedio[i] = (alumnos_con_notas[i][0]+alumnos_con_notas[i][1]) / 2     #guardo en el nuevo diccionario el nombre del alumno con su respectivo promedio
    return alumnos_promedio

alumnos_con_promedio = promedio_alumno(alumnos_con_notas)
print (alumnos_con_promedio)

print ("="*90)

# 3. Calcular el promedio general del curso.

def promedio_curso (alumnos_con_promedio):                                              #obtengo el promedio de todo los alumnos 
    curso_prom =0                                                                       #auxiliar contador de total
    for i in alumnos_con_promedio.keys():                                               #itero mediante las keys para despues poder acceder al valor
        curso_prom+= alumnos_con_promedio[i]                                            #sumo al auxiliar la nota de cada alumno
    curso_prom = curso_prom / len(alumnos_con_promedio)                                 #divido por la longitud del diccionario, que son el total de alumnos y asi obtengo el promedio
    return curso_prom

promedio_del_curso = promedio_curso (alumnos_con_promedio)
print (promedio_del_curso)

print ("="*90)

# 4. Identificar al estudiante con la nota promedio más alta.

def promedio_mas_alto (alumnos_con_promedio):                                           #obtengo el alumno con promedio mas alto
    max_prom = max(alumnos_con_promedio, key=alumnos_con_promedio.get)                  #utilizo max para sacar el maximo, junto al argumento key que aplica la funcion .get a cada elemento antes de comprar para el maximo
#                                                                                        asi obtengo el valor de cada elemento, y comparo en base a eso para calcular max (o eso entendi) sino obtengo el ultimo elemento 
    return max_prom

promedio_maximo = promedio_mas_alto(alumnos_con_promedio)
print (promedio_maximo)

print ("="*90)

# 5. Identificar al estudiante con la nota más baja.

def nota_mas_baja (alumnos_con_notas):                                                 #obtengo el alumno con la nota mas baja
    min_nota = min(alumnos_con_notas, key=lambda x: min(alumnos_con_notas[x]))         #utilizo min para sacar el minimo, uso el argumento key con un lambda donde calculo el minimo entre los dos elementos de la lista
#                                                                                       para luego comprar el minimo de todos los alumnos utilizando el minimo de cada alumno    
    return min_nota

nota_minima = nota_mas_baja(alumnos_con_notas)
print (nota_minima)

print ("="*90)