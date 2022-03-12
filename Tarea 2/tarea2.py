from array import *
from gpiozero import Button
import random
import argparse
import time
import threading


parser = argparse.ArgumentParser() #uso de argparse para ingresar el dato
parser.add_argument('tamano', metavar='tamano', type=int, help='ingrese el tamano del array')
args= parser.parse_args()
tamano=args.tamano

boton= Button(2)# Se declara el boton

Arr= array('I') # Se declara el array 
Res=0           # Variable global para los threads

def SumSerie(*self):#Suma cada elemento
    Suma=0
    for i in Arr:
        Suma+=i
        time.sleep(0.1)
    return Suma

def SumConcurrente(thrd):#Funcion para el thread, recibe el num del thread
    global Res
    k=len(Arr)//4
    SumC=0
    residuo=(len(Arr)-(4*k))
    for i in range(k): #Se suma de 4 en 4
        SumC+=Arr[thrd+(4*i)]
        time.sleep(0.1)
        
    if thrd>=residuo:
        Res+=SumC
        time.sleep(0.1)
        return SumC
        
    else:
        SumC+=Arr[(4*k)+thrd]# casos para cuando el tamano no es multiplo de 4
        time.sleep(0.1)
        Res+=SumC
        time.sleep(0.1)
        return SumC
    
boton.wait_for_press() # Espera hasta detectar que se oprimio el boton    
    
    
for i in range (tamano): #Llena el Array con ints 
    #Arr.append(random.randint(0,100))
    Arr.append(i)

#Se hace la suma uno por uno
tiempo1=time.time()
SumS=SumSerie()
tiempo1 = time.time()-tiempo1# Toma el tiempo de sumado uno por uno 

t0=threading.Thread(target =SumConcurrente, name= 'thread0', args=[0])#Declaran los threads 
t1=threading.Thread(target =SumConcurrente, name= 'thread1', args=[1])
t2=threading.Thread(target =SumConcurrente, name= 'thread2', args=[2])
t3=threading.Thread(target =SumConcurrente, name= 'thread3', args=[3])

#se comienzan los threads para la suma concurrente
tiempo2=time.time()
t0.start()
t1.start()
t2.start()
t3.start()

t0.join()
t1.join()
t2.join()
t3.join()
tiempo2 = time.time()-tiempo2# Toma el tiempo de la suma concurrente

print(Arr)
print('Metodo 1:', tiempo1,'s')
print('Resultado:', SumS)

print('Metodo 2:',tiempo2,'s')
print('Resultado:', Res)
