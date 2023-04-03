#9. Escriba un programa que solicite por teclado una palabra y calcule el valor de la misma dada la siguiente tabla de valoresdel juego scrabble:

letter={
    'a':1,'e':1,'i':1,'o':1,'l':1,'n':1,'r':1,'s':1,'t':1,
    'd':2,'g':2,
    'b':3,'c':3,'m':3,'p':3,
    'f':4,'h':4,'v':4,'w':4,'y':4,
    'k':5,
    'j':8,'x':8,
    'q':10,'z':10    
    }

word=input("Ingrese una palabra para calcular el valor: ")
sum=0
for i in word.lower():
    sum +=letter[i]

print (F"Palabra: {word} \n valor: {sum}")