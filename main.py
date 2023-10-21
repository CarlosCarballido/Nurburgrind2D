
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import csv
from cone.cone import cono_azul, cono_amarillo

# Rutas a los archivos
ruta_mapa_nurbur2D = 'utils/nurburgring_map_2D.jpg'
ruta_csv_nurbur = 'data/nurbur_data.csv'

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

limite_izquierdo = np.array([[cono.x for cono in conos_azules], [cono.y for cono in conos_azules]])
limite_derecho = np.array([[cono.x for cono in conos_amarillos], [cono.y for cono in conos_amarillos]])

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

# Número de puntos intermedios a agregar entre cada par de puntos
num_puntos_intermedios = 60  # Puedes ajustar este valor según tus necesidades

# Inicializa un nuevo array para almacenar los puntos con interpolación
nueva_trazada_intermedia = []

# Recorre la trazada original para agregar puntos intermedios
for i in range(len(trazada_intermedia) - 1):
    x1, y1 = trazada_intermedia[i]
    x2, y2 = trazada_intermedia[i + 1]
    
    # Calcula la distancia entre los dos puntos
    distancia_entre_puntos = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    # Interpola los puntos intermedios solo si la distancia es mayor que un umbral
    if distancia_entre_puntos > 0.01:  # Puedes ajustar este umbral según tus necesidades
        interp_x = np.linspace(x1, x2, num_puntos_intermedios + 2)[1:-1]
        interp_y = np.linspace(y1, y2, num_puntos_intermedios + 2)[1:-1]
        nueva_trazada_intermedia.extend(list(zip(interp_x, interp_y)))
    else:
        nueva_trazada_intermedia.append([x1, y1])

# Agrega el último punto de la trazada original
nueva_trazada_intermedia.append(trazada_intermedia[-1])

# Convierte la lista de puntos en un array numpy
trazada_intermedia = np.array(nueva_trazada_intermedia)

plt.figure(figsize=(10, 6))
plt.imshow(background_image)

for i in range(len(limite_derecho[0])):
    plt.scatter(limite_derecho[0][i], limite_derecho[1][i], c="yellow")

for i in range(len(limite_izquierdo[0])):
    plt.scatter(limite_izquierdo[0][i], limite_izquierdo[1][i], c="blue")
    
# Inicializar el punto rojo en la primera posición
punto_rojo = plt.scatter(trazada_intermedia[0, 0], trazada_intermedia[0, 1], c="red")
    
plt.plot(trazada_intermedia[:, 0], trazada_intermedia[:, 1], 'g-', label='Trazada intermedia')

plt.title('Representación en 2D del Circuito de Nürburgring')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.legend()

plt.grid(True)

# Actualizar la posición del punto rojo en un bucle
for i in range(1, len(trazada_intermedia)):
    x, y = trazada_intermedia[i]
    punto_rojo.set_offsets([x, y])
    plt.pause(0.01)  # Añadir un retraso de 0.1 segundos entre actualizaciones

plt.show()