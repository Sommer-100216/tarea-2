import streamlit as st

st.title("Reconocedor de la letra T")

st.write("Ajusta los pesos y observa cómo cambia la puntuación.")

# -------------------------
# Imágenes
# -------------------------

imagenes = {
    "T 1": [
        [1,1,1],
        [0,1,0],
        [0,1,0]
    ],

    "T 2": [
        [1,1,1],
        [0,1,0],
        [1,1,1]
    ],

    "T 3": [
        [1,1,1],
        [0,1,0],
        [0,1,1]
    ],

    "No T 1": [
        [0,1,0],
        [1,1,1],
        [0,1,0]
    ],

    "No T 2": [
        [1,0,1],
        [1,1,1],
        [0,0,0]
    ],

    "No T 3": [
        [1,1,0],
        [1,1,0],
        [0,1,0]
    ]
}

# -------------------------
# Selección imagen
# -------------------------

nombre = st.selectbox(
    "Selecciona una imagen",
    list(imagenes.keys())
)

imagen = imagenes[nombre]

st.write("Imagen seleccionada:")

for fila in imagen:
    st.text(" ".join(map(str, fila)))
    
# -------------------------
# Pesos ajustables
# -------------------------

st.subheader("Pesos")

pesos = []

for i in range(3):
    fila = []
    cols = st.columns(3)

    for j in range(3):
        valor = cols[j].slider(
            f"W{i}{j}",
            min_value=-5,
            max_value=5,
            value=1,
            key=f"{i}{j}"
        )
        fila.append(valor)

    pesos.append(fila)

# -------------------------
# Threshold opcional
# -------------------------

threshold = st.slider(
    "Threshold",
    min_value=-20,
    max_value=20,
    value=5
)

# -------------------------
# Cálculo manual
# -------------------------

puntaje = 0

for i in range(3):
    for j in range(3):
        puntaje += imagen[i][j] * pesos[i][j]

st.subheader("Resultado")

st.write("Puntaje total:", puntaje)
st.write("Threshold actual:", threshold)

if puntaje >= threshold:
    st.success("La máquina piensa que es una T")
else:
    st.error("La máquina piensa que NO es una T")
