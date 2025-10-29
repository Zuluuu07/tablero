import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("Tablero para dibujo")

with st.sidebar:
    st.subheader("Propiedades del tablero")

st.subheader("Dimensiones del tablero")
canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)

# herramienta y grosor del trazo
drawing_mode = st.selectbox(
    "Herramienta de dibujo:",
    ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
)
stroke_width = st.slider("Grosor del trazo", 1, 25, 3)

# colores
stroke_color = st.color_picker("Color de trazo", "#FFFFFF")
bg_color = st.color_picker("Color de fondo", "#000000")

# lienzo
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}",
)
