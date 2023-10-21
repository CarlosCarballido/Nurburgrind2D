import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import csv

class cono_azul:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "Cono azul en la posición: ({}, {})".format(self.__x, self.__y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

class cono_amarillo:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "Cono amarillo en la posición: ({}, {})".format(self.__x, self.__y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

# Rutas a los archivos
ruta_mapa_nurbur2D = 'utils/nurburgring_map_2D.jpg'
ruta_csv_nurbur = 'nurbur_data.csv'

background_image = mpimg.imread(ruta_mapa_nurbur2D)

conos_azules = []
conos_amarillos = []

with open(ruta_csv_nurbur, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        cono_azul_obj = cono_azul(float(row['X_izq']), float(row['Y_izq']))
        conos_azules.append(cono_azul_obj)
        cono_amarillo_obj = cono_amarillo(float(row['X_der']), float(row['Y_der']))
        conos_amarillos.append(cono_amarillo_obj)


l = np.array([[1,2,3,4], [5,6,7,8]])
print(l[0][0])
limite_izquierdo = np.array([[cono.x for cono in conos_azules], [cono.y for cono in conos_azules]])
limite_derecho = np.array([[cono.x for cono in conos_amarillos], [cono.y for cono in conos_amarillos]])

print(limite_izquierdo)
print(limite_derecho)
# Inicializa una lista para almacenar los puntos medios
puntos_medios = []

# Recorre los conos izquierdos y derechos para calcular los puntos medios
for i in range(len(limite_izquierdo[0])):
    x_izquierdo = limite_izquierdo[0][i]
    y_izquierdo = limite_izquierdo[1][i]
    x_derecho = limite_derecho[0][i]
    y_derecho = limite_derecho[1][i]
    
    # Calcula el punto medio
    punto_medio_x = (x_izquierdo + x_derecho) / 2
    punto_medio_y = (y_izquierdo + y_derecho) / 2
    
    # Agrega el punto medio a la lista de puntos medios
    puntos_medios.append([punto_medio_x, punto_medio_y])

# Convierte la lista de puntos medios en un array numpy
trazada_intermedia = np.array(puntos_medios)

plt.figure(figsize=(10, 6))
plt.imshow(background_image)

for i in range(len(limite_derecho[0])):
    plt.scatter(limite_derecho[0][i], limite_derecho[1][i], c="yellow")

for i in range(len(limite_izquierdo[0])):
    plt.scatter(limite_izquierdo[0][i], limite_izquierdo[1][i], c="blue")
    
plt.plot(trazada_intermedia[:, 0], trazada_intermedia[:, 1], 'g-', label='Trazada intermedia')

plt.title('Representación en 2D del Circuito de Nürburgring')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.legend()

plt.grid(True)
plt.show()
