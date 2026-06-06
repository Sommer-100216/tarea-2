# tarea-2
Construir un sistema interactivo capaz de asignar puntajes a mini-imágenes binarias para determinar qué tan similares son a una letra T.
En este curso hemos estudiado distintas preguntas fundamentales de la teoría de la computación:

¿Cómo calculan las máquinas?
¿Cómo aprenden las máquinas?
¿Cuáles son los límites de lo que una máquina puede calcular?
En la tarea anterior construimos un perceptrón simple para clasificar compuertas lógicas como AND y OR, y observamos las limitaciones del modelo frente a XOR.

En esta nueva etapa comenzaremos a explorar cómo una máquina puede reconocer patrones visuales simples ajustando parámetros numéricos.

Objetivo de la actividad
Construir un sistema interactivo capaz de asignar puntajes a mini-imágenes binarias para determinar qué tan similares son a una letra T.

El objetivo NO es utilizar librerías modernas de inteligencia artificial, sino comprender intuitivamente cómo una máquina puede transformar números en decisiones.

Restricción importante
NO se permite usar:
TensorFlow
PyTorch
Scikit-Learn
Keras
OpenCV
Librerías de Machine Learning
Librerías de Deep Learning
La clasificación debe implementarse manualmente utilizando únicamente:

Python básico
listas o matrices simples
operaciones matemáticas básicas
Idea central
Cada imagen será representada como una matriz binaria pequeña.

Ejemplo positivo — letra T
1 1 1
0 1 0
0 1 0
Ejemplo negativo
0 1 0
1 1 1
0 1 0
Cada posición representa un pixel:

1 → pixel activo
0 → pixel apagado
Primera etapa: cálculo manual
En esta primera parte NO construiremos todavía un clasificador automático completo.

El objetivo será construir una “máquina de puntuación”.

La máquina debe:

Multiplicar cada pixel por un peso.
Sumar los resultados.
Mostrar el puntaje total obtenido.
Fórmula general
y = Σ(wᵢxᵢ)
Parte interactiva
El sistema debe permitir modificar manualmente:

los pesos
y opcionalmente el threshold
La actividad debe funcionar como un pequeño juego experimental donde el estudiante:

ajusta parámetros
prueba imágenes
observa resultados
y trata de aumentar la puntuación de las Ts reales
Opciones de implementación
Debes elegir UNA:

Opción A — Jupyter Notebook
Usando:

Python
ipywidgets
Opción B — Streamlit
Aplicación interactiva desplegada localmente o en la nube.

Requisitos mínimos
1. Imágenes binarias
Definir al menos:

3 imágenes tipo T
3 imágenes que NO sean T
2. Sistema de pesos
Cada posición debe tener un peso ajustable.

[
 [ 2, 2, 2],
 [-1, 3,-1],
 [-1, 3,-1]
]
3. Puntaje total
El programa debe mostrar:

el cálculo total
y cómo cambia al mover las “perillas”
Entregables
código fuente
notebook o enlace de Streamlit
breve explicación del funcionamiento
Reflexión conceptual
¿Qué partes de la imagen parecen más importantes?
¿Qué ocurre cuando modificas ciertos pesos?
¿Qué imágenes generan resultados ambiguos?
¿Qué relación encuentras entre esta actividad y la idea de “aprendizaje”?
