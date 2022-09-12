#desafio 16
import random
import math
 
num = float(input('digite o numero:'));
num1 = math.trunc(num);
print(num1);
#desafio 18
num2 = float(input('digite o seno:'));
num3 = float(input('digite o coseno:'));
num4 = float( input ('digite a tangete:'));
sen = math.sin(math.radians(num2));
cos = math.cos(math.radians(num3));
tang = math.tan(math.radians(num4)) 
print(' o seno: {}, o coseno: {}, a tangete {} '.format(sen, cos, tang));
#desafio19
nom = str (input ('digite o nome do aluno 1:'));
nom2 = str (input ('digite o nome do aluno 2:'));
nom3 = str (input ('digite o nome do aluno 3:'));
nom4 = str (input ('digite o nome do aluno 4:'));
lista = [nom, nom2, nom3, nom4];
sorteio = random.choice(lista);
print (sorteio);
#desafio20
nom = str (input ('digite o nome do aluno 1:'));
nom2 = str (input ('digite o nome do aluno 2:'));
nom3 = str (input ('digite o nome do aluno 3:'));
nom4 = str (input ('digite o nome do aluno 4:'));
lista = [(nom), (nom2), (nom3), (nom4)];
sorteio = random.sample(lista, 4);
print (sorteio);
 

    

