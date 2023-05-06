import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

malla= pd.Series(["No 4","No 10","No 20","No 40","No 60","No 140","No 200"])
malla
abertura= pd.Series([4.75,2,.85,.425,.25,.106,.075])
abertura
retenido=pd.Series([15.5,25.8,60.5,40.2,41.2,15.2,13.2])
retenido
otro=pd.DataFrame({
    "tamices":malla,
    "abertura (mm)":abertura,
    "retenido":retenido
})
otro
otro["retenido_acumulado"]=(otro["retenido"]).cumsum()
otro
otro["pasa"]=(otro["retenido"]).sum()-(otro["retenido_acumulado"])
otro
otro["% pasa"]=(otro["pasa"])/(otro["retenido"]).sum()*100
otro
def graficaGranulometrica():
  abertura = np.array(otro["abertura (mm)"]) # se llaman los datos de la tabla como una variable
  pasa = np.array(otro["% pasa"]) # se llaman los datos de la tabla como una variable
  plt.figure(figsize=(14, 4)) # se alarga mas el eje  x con respecto al eje y
  plt.plot(abertura,pasa,linestyle='-', marker='o', color='k', fillstyle='none',label='Data') #se grafica la linea de granulometria con la abertura en las x y el % pasa en y
  f = interp1d(pasa, abertura) # se usa una funcion para interpolar la linea granulometrica y conocer los valores de x conociendo los D60,D50.....
  y1_coord = 60
  y2_coord = 50
  y3_coord = 30
  y4_coord = 10
  x1_coord = f(y1_coord)
  x2_coord = f(y2_coord)
  x3_coord = f(y3_coord)
  x4_coord = f(y4_coord)
  x1_formatted = '{:.2f}'.format(x1_coord)
  x2_formatted = '{:.2f}'.format(x2_coord)
  x3_formatted = '{:.2f}'.format(x3_coord)
  x4_formatted = '{:.2f}'.format(x4_coord)
  plt.scatter(x1_coord, y1_coord, marker='s', s=50, color='k', label='D60='+x1_formatted) # Se estima el valor de los D y se coloca en una tabla resumen con el simbolo representativo
  plt.scatter(x2_coord, y2_coord, marker='<', s=50, color='k', label='D50='+x2_formatted)
  plt.scatter(x3_coord, y3_coord, marker='>', s=50, color='k', label='D30='+x3_formatted)
  plt.scatter(x4_coord, y4_coord, marker='^', s=50, color='k', label='D10='+x4_formatted)
  plt.title("",fontsize=10)
  plt.xlabel('Diámetro (mm)')
  plt.ylabel('Porcentaje pasa acumulado (%)')
  plt.title('Curva granulométrica')
  plt.legend() #crea un historico
  plt.xscale("log")
  plt.xlim(0.001,100) #Se limita hasta donde van los valores x de la grafica
  plt.ylim(-10,100) #Se limita hasta donde van los valores y de la grafica
  plt.grid(color='k',lw='0.1',ls='-')
  x = [1, 10, 100, 5, 50, 20, 2, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]
  plt.xticks(x, x, fontsize=8)
  ax1 = plt.gca()
  ax1.invert_xaxis()
  plt.text(85, -9, r'Rocas', fontsize=8, rotation=90) #Se colocan los textos de los limites de particulas en sentido vertical
  plt.text(22, -9, r'Grava(Gruesa)', fontsize=8, rotation=90)
  plt.text(5.4, -9, r'Grava(Fina)', fontsize=8, rotation=90)
  plt.text(2.2, -9, r'Arena(Gruesa)', fontsize=8, rotation=90)
  plt.text(0.5, -9, r'Arena(Mediana)', fontsize=8, rotation=90)
  plt.text(0.09, -9, r'Arena(Fina)', fontsize=8, rotation=90)
  plt.text(0.011, -9, r'Coloides', fontsize=8, rotation=90)
  plt.text(0.0055, -9, r'Limo', fontsize=8, rotation=90)
  plt.text(0.0011, -9, r'Arcilla', fontsize=8, rotation=90)
  # Agregar el segundo eje x para los nombres de los tamices
  malla1 = ["3","2-1/2","2","1-1/2","1","3/4","1/2","3/8","No. 4","No. 6","No. 8","No. 10","No. 16","No. 20","No. 30","No. 40","No. 50","No. 60","No. 80","No. 100","No. 140","No. 170","No. 200"]
  abertura1=([75, 63, 50, 37.5, 25, 19, 12.5, 9.5, 4.75,3.35,2.36, 2,1.18,.85,0.6, .425,0.3,.25,0.18,0.15,.106,.09,.075])
  ax2 = ax1.twiny()
  ax2.set_xscale('log')
  ax2.set_xticks(abertura1)
  ax2.set_xticklabels(malla1, rotation=90, fontsize=8)
  y=(-10,0,20,40,60,80,100)
  ax1.set_yticklabels(y, fontsize=8)
  ax2.set_xlabel('Tamices')
  ax2.set_xlim(0.001,100)
  ax2.invert_xaxis()
  LL1 = ([75,75]) #Conjunto de valores 
  LL2 = ([19,19]) #Conjunto de valores 
  LL3 = ([4.75,4.75]) #Conjunto de valores 
  LL4 = ([2,2]) #Conjunto de valores 
  LL5 = ([0.425,0.425]) #Conjunto de valores 
  LL6 = ([0.075,0.075]) #Conjunto de valores 
  LL7 = ([0.01,0.01]) #Conjunto de valores 
  LL8 = ([0.005,0.005]) #Conjunto de valores
  LL9 = ([0.001,0.001]) #Conjunto de valores 
  LL10 = ([-10,100])
  plt.plot(LL1, LL10,color='grey', lw='0.8', ls='--')
  plt.plot(LL2, LL10,color='grey', lw='0.8', ls='--')
  plt.plot(LL3, LL10,color='grey', lw='0.8', ls='--')
  plt.plot(LL4, LL10,color='grey', lw='0.8', ls='--') # se realiza la linea punteada de los tamices limite
  plt.plot(LL5, LL10,color='grey', lw='0.8', ls='--')
  plt.plot(LL6, LL10,color='grey', lw='0.8', ls='--')
  plt.plot(LL7, LL10,color='grey', lw='0.8', ls='--')
  plt.plot(LL8, LL10,color='grey', lw='0.8', ls='--')
  plt.plot(LL9, LL10,color='grey', lw='0.8', ls='--')
  plt.axvline(x=63, ymin=-10, ymax=100, color='grey', ls='-',lw='0.3')
  plt.axvline(x=37.5, ymin=-10, ymax=100, color='grey', ls='-',lw='0.3')
  plt.axvline(x=25, ymin=-10, ymax=100, color='grey', ls='-',lw='0.3')
  plt.axvline(x=12.5, ymin=-10, ymax=100, color='grey', ls='-',lw='0.3')
  plt.axvline(x=9.5, ymin=-10, ymax=100, color='grey', ls='-',lw='0.3')
  plt.axvline(x=3.35, ymin=-10, ymax=100, color='grey', ls='-',lw='0.3')
  plt.axvline(x=2.36, ymin=-10, ymax=100, color='grey', ls='-',lw='0.3')
  plt.axvline(x=1.18, ymin=-10, ymax=100, color='grey', ls='-',lw='0.3')
  plt.axvline(x=0.6, ymin=-10, ymax=100, color='grey', ls='-',lw='0.3')
  plt.axvline(x=0.85, ymin=-10, ymax=100, color='grey', ls='-',lw='0.3')
  plt.axvline(x=0.3, ymin=-10, ymax=100, color='grey', ls='-',lw='0.3')
  plt.axvline(x=.25, ymin=-10, ymax=100, color='grey', ls='-',lw='0.3')
  plt.axvline(x=.18, ymin=-10, ymax=100, color='grey', ls='-',lw='0.3')
  plt.axvline(x=.15, ymin=-10, ymax=100, color='grey', ls='-',lw='0.3')
  plt.axvline(x=.106, ymin=-10, ymax=100, color='grey', ls='-',lw='0.3')
  plt.axvline(x=.09, ymin=-10, ymax=100, color='grey', ls='-',lw='0.3')
  plt.show()