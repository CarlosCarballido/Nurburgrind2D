import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import csv

class cono_azul:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    def __str__(self):
        return "Cono azul en la posición: ({}, {})".format(self.x, self.y)
    
    @property
    def cono_azul(self):
        return self.__cono_azul
    
    @cono_azul.setter
    def cono_azul(self, x, y):
        self.__x = x
        self.__y = y
        
class cono_amarillo:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    def __str__(self):
        return "Cono amarillo en la posición: ({}, {})".format(self.x, self.y)
    
    @property
    def cono_amarillo(self):
        return self.__cono_amarillo
    
    @cono_amarillo.setter
    def cono_amarillo(self, x, y):
        self.__x = x
        self.__y = y

x_izq = []
y_izq = []
x_der = []
y_der = []

# Rutas a los archivos
ruta_mapa_nurbur2D = 'utils/nurburgring_map_2D.jpg'
ruta_csv_nurbur = 'nurbur_data.csv'

with open(ruta_csv_nurbur, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        x_izq.append(float(row['X_izq']))
        y_izq.append(float(row['Y_izq']))
        x_der.append(float(row['X_der']))
        y_der.append(float(row['Y_der']))

background_image = mpimg.imread(ruta_mapa_nurbur2D)

limite_derecho = np.array([[1, 1], [1, 1]])
limite_izquierdo = np.array([[1, 1], [1, 1]])
trazada_intermedia = np.array([[1, 1], [1, 1]])

plt.figure(figsize=(10, 6))
plt.imshow(background_image)

plt.plot(limite_derecho[:, 0], limite_derecho[:, 1], 'yo-', label='Límite derecho')
plt.plot(limite_izquierdo[:, 0], limite_izquierdo[:, 1], 'bo-', label='Límite izquierdo')
plt.plot(trazada_intermedia[:, 0], trazada_intermedia[:, 1], 'g-', label='Trazada intermedia')

plt.title('Representación en 2D del Circuito de Nürburgring')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.legend()

plt.grid(True)
plt.show()
