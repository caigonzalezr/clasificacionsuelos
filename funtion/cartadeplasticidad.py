import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

def graficaPlasticidad():
  LL = ([10,77]) #Conjunto de valores 
  LL1 = ([0,60]) #Conjunto de valores 
  LL2 = ([20,100]) #Conjunto de valores 
  LL3 = ([0,58]) #Conjunto de valores 
  LL4 = ([60,60]) #Conjunto de valores 
  LL5 = ([0,60]) #Conjunto de valores 
  LL6 = ([0,100]) #Conjunto de valores 
  LL7 = ([40,40]) #Conjunto de valores 
  LL8 = ([50,50]) #Conjunto de valores 
  LL9 = ([0,60]) #Conjunto de valores 
  LL10 = ([50,100]) #Conjunto de valores 
  LL11 = [22,58] #Conjunto de valores 
  LL12 = [50,100,100,77,50] #Conjunto de valores 
  LL13 = [22,58,60,60,36] #Conjunto de valores 
  LL14 = [20,50,50] #Conjunto de valores 
  LL15 = [0,22,0] #Conjunto de valores 
  LL16 = [10,14,25,20] #Conjunto de valores 
  LL17 = [0,4,4,0] #Conjunto de valores 
  LL18 = [14,18,30,25] #Conjunto de valores 
  LL19 = [4,7,7,4] #Conjunto de valores 
  LL20 = [18,50,50,30] #Conjunto de valores 
  LL21 = [7,36,22,7] #Conjunto de valores 
  plt.plot(LL2, LL3, 'b-', label = "Linea A") #se grafica la linea A con el conjunto de valores, el primero comprende las coordenadas de x y el segundo las de y
  plt.plot(LL, LL1, 'k', ls=':', label = "Linea U") #se grafica la linea U con el conjunto de valores, el primero comprende las coordenadas de x y el segundo las de y
  plt.plot(LL4, LL5, 'k', ls='--') #se grafica una linea punteada con el conjunto de valores, el primero comprende las coordenadas de x y el segundo las de y
  plt.plot(LL6, LL7, 'k', ls='--') #se grafica una linea punteada con el conjunto de valores, el primero comprende las coordenadas de x y el segundo las de y
  plt.plot(LL8, LL9, 'g-') #se grafica una linea continua de color verde, el primero comprende las coordenadas de x y el segundo las de y
  plt.grid(color='k',lw='0.1',ls='-') #se grafica la grilla con un color, espesor de linea y tipo de linea
  plt.title("CARTA DE PLASTICIDAD", fontsize=10) #titulo del grafico
  plt.xlabel("LIMITE LIQUIDO",fontsize=10) #titulo del eje x
  plt.ylabel("INDICE DE PLASTICIDAD",fontsize=10) #titulo del eje y
  plt.legend() #muestra las convenciones de las lineas A Y U
  plt.fill_between(LL10,0,LL11,color='pink') #Sombrea un area en especifico por medio de un rango, un valor minimo y una funcion
  plt.fill(LL12,LL13,color='lightgreen') #Sombrea un area en especifico por medio de coordenadas
  plt.fill(LL14,LL15,color='skyblue') #Sombrea un area en especifico por medio de coordenadas
  plt.fill(LL16,LL17,color='skyblue') #Sombrea un area en especifico por medio de coordenadas
  plt.fill(LL18,LL19,color='magenta') #Sombrea un area en especifico por medio de coordenadas
  plt.fill(LL20,LL21,color='yellow') #Sombrea un area en especifico por medio de coordenadas
  plt.xlim(0,100) #Se limita hasta donde van los valores x de la grafica
  plt.ylim(0,60) #Se limita hasta donde van los valores y de la grafica
  plt.scatter(60,40, color='r') #se grafica un punto con ciertas coordenadas
  plt.text(17, 5, r'CL-ML', fontsize=9) #se grafica un texto en ciertas corrdenas y cierto tamaño
  plt.text(35, 5, r'ML', fontsize=9) #se grafica un texto en ciertas corrdenas y cierto tamaño
  plt.text(81, 21, r'MH', fontsize=9) #se grafica un texto en ciertas corrdenas y cierto tamaño
  plt.text(81, 55, r'LL', fontsize=9) #se grafica un texto en ciertas corrdenas y cierto tamaño
  plt.text(62, 40, r'CH', fontsize=9) #se grafica un texto en ciertas corrdenas y cierto tamaño
  plt.text(12, 21, r'LP', fontsize=9) #se grafica un texto en ciertas corrdenas y cierto tamaño
  plt.text(15, 38, r'NO EXISTE', fontsize=10) #se grafica un texto en ciertas corrdenas y cierto tamaño
  plt.text(31, 15, r'CL', fontsize=9) #se grafica un texto en ciertas corrdenas y cierto tamaño
  plt.show() #mostrar el grafico