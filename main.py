import json

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time
from datetime import date, datetime
import tkinter as tk
from login import login_page_usuario
from login import login_page_monitor

##titulo

col10, col20, col30 = st.columns(3)
col10.image('liceo_habits.png', width= 150 )

col20.markdown("<h1 style='text-align: center; color: black; font-family: calibri; '>LICEO HABITS</h1>", unsafe_allow_html=True)
st.write("---")
#horario del curso 1101

horario_1101 = pd.DataFrame({
    'lunes': ['Electronica', 'Electronica', 'Calculo', 'Ingles', 'Ingles', 'Ptp', 'Ptp'],
    'martes': ['Fisica','Fisica','G.ambiental','Edu_Fisica','Religion','Quimica', 'Quimica'],
    'miercoles': ['Calculo', 'Calculo', 'Ingles','D_curso', 'Lengua', 'Lengua','salida_temprano'],
    'jueves': ['Filosofia', 'Filosofia', 'Artistica', 'Tecnologia', 'Catedra_F', 'Fisica', 'Form_int'],
    'viernes': ['Quimica', 'Quimica', 'Informatica', 'Lengua', 'Lengua', 'Investigacion', 'Investigacion'],
    })

#cambiar de pagina de inicio de sesion al organizador

def iniciar_estudiante():
    # st.markdown("<h3 style='text-align: center; color: black; font-family: sans-serif; '>INICIO SESION USUARIO</h3>", unsafe_allow_html=True)
    # st.write("")
    # st.write("")
    # st.write("")
    # st.write("")
    # st.write("")
    if "logged_in_usuario" not in st.session_state:
        st.session_state["logged_in_usuario"] = False
    
    if "estudiante" not in st.session_state:
        st.session_state["estudiante"] = ""

    if not st.session_state["logged_in_usuario"]:
        login_page_usuario()
    else:
        proyecto()

#pagina inicio sesion monitor
        
def iniciar_monitor():
    # st.markdown("<h3 style='text-align: center; color: black; font-family: sans-serif; '>INICIO SESION MONITOR</h3>", unsafe_allow_html=True)
    # st.write("")
    # st.write("")
    # st.write("")
    # st.write("")
    # st.write("")
    if "logged_in_monitor" not in st.session_state:
        st.session_state["logged_in_monitor"] = False

    if not st.session_state["logged_in_monitor"]:
        login_page_monitor()
    
    else:
        definir_tarea()
    

#pagina del organizador de tareas|


def proyecto():
    st.markdown("<h3 style='text-align: center; color: black; font-family: calibri;'>ORGANIZADOR DE TAREAS</h3>", unsafe_allow_html=True)
    st.write("")
    st.write(
        "Bienvenido al organizador de tareas, en este lugar encontraras un programa en el cual podras ver "
        "las tareas que tienes pendientes, organizadas segun la prioridad de tiempo; en la prioridad "
        "alta, encontraras las tareas que son para entregarse en un lapso menor o igual a 3 dias."
        "Por otro lado en la parte de prioridad media, encontraras las tareas que son para una fecha "
        "mayor a 3 dias pero menor a 5. Por ultimo en la seccion de prioridad baja encontraras "
        "las tareas que son para entregar en una fecha mayor a 7 dias."
        )
    st.write("---")
    st1,st2,st3 = st.columns(3)
    st1.markdown("<h5 style='text-align: center; color: black; font-family: calibri;'>PRIORIDAD ALTA</h5>", unsafe_allow_html=True)
    st2.markdown("<h5 style='text-align: center; color: black; font-family: calibri;'>PRIORIDAD MEDIA</h5>", unsafe_allow_html=True)
    st3.markdown("<h5 style='text-align: center; color: black; font-family: calibri;'>PRIORIDAD BAJA</h5>", unsafe_allow_html=True)
    st.write("")
    
    estudiante = st.session_state["estudiante"]
    base_datos = cargar_bd()
    

    _datos_estudiante = list(filter(lambda x: x["id"]== estudiante, base_datos))
    _datos_sin_estudiante = list(filter(lambda x: x["id"]!= estudiante, base_datos))

    datos_estudiante = _datos_estudiante[0]

    for tarea in datos_estudiante["lista_tareas"]:
        if tarea["estado"]:
            with st.form(f"f{tarea}{tarea["fecha"]}"):
                col100, col200, col300 = st.columns(3)

                # crear variable con la fecha del dia presente ("d/m/Y")
                # obtener string de la fecha de entrega de la tarea y transformar a datetime
                # contar dias de diferencia entre fecha presente y fecha entrega
                # crear condicional de columnas según la cantidad de días

                fecha_presente = datetime.now()
                fecha_tarea = datetime.strptime(tarea["fecha"], "%d/%m/%Y")
                delta = fecha_tarea - fecha_presente
                delta_dias = delta.days

                if delta_dias <= 3:
                    marcar = col100.form_submit_button(
                    label=f"{tarea["asignatura"]} - {tarea["fecha"]} - descripcion: {tarea["descripcion"]}"
                )
                elif delta_dias<7 :
                    marcar = col200.form_submit_button(
                    label=f"{tarea["asignatura"]} - {tarea["fecha"]} - descripcion: {tarea["descripcion"]}"
                )
                else:
                    marcar = col300.form_submit_button(
                    label=f"{tarea["asignatura"]} - {tarea["fecha"]} - descripcion: {tarea["descripcion"]}"
                )
            # marcar
            if marcar:
                tarea["estado"] = False
                _datos_sin_estudiante.append(datos_estudiante)
                actualizar_bd(_datos_sin_estudiante)
                st.rerun()

    # col1, col2, col3, col4 = st.columns(4)

    # Titulo1 = col1.write("PRIORIDAD MUY ALTA")
    # punto1_1 = col1.button("Calculo")
    # punto1_2 = col1.button("Ingles")
    # punto1_3 = col1.button("Lengua")
    # Titulo2 = col2.write("PRIORIDAD ALTA")
    # punto2_1 = col2.button("Fisica")
    # punto2_2 = col2.button("Quimica")
    # Titulo3 = col3.write("PRIORIDAD MEDIA")
    # punto3_1 = col3.button("Educacion Fisica")
    # Titulo4 = col4.write("PRIORIDAD BAJA")
    # punto4_1 = col4.button("Artes")


#pagina de descripcion de la actividad


def vista_ampliada_tarea():
    materia = "matematicas"
    st.markdown("<h1 style='text-align: center; color: black;'> MATEMATICAS </h1>", unsafe_allow_html=True)
    firstcolum, secondcolum = st.columns(2)
    firstcolum.write("## Actividad:")
    firstcolum.write("Infografia")
    secondcolum.write("")
    secondcolum.write("")
    secondcolum.write("")
    secondcolum.write("")
    secondcolum.button("**Ya la realice**")
    st.write("---")
    st.write("FECHA DE ENTREGA:")
    st.write("25/02/2024")

def cargar_bd():
    bd = None
    with open("base_estudiantes.json", encoding="utf-8") as file:
        bd = json.load(file)
    return bd

def actualizar_bd(base_datos):
    with open("base_estudiantes.json", encoding="utf-8", mode="w") as file:
        json.dump(base_datos, file)

#pagina de tarea nueva

def definir_tarea():
    st.markdown("<h3 style='text-align: center; color: black; font-family: sans-serif;'> ASIGNACION DE TAREAS </h3>", unsafe_allow_html=True)
    st.write("")
    st.write(
        "Bienvenido Monitor, en esta seccion podras subir las actividades que se dejen en las diferentes "
        "asignaturas, lo primero que debes hacer es seleccionar la asignatura de la tarea, luego debes"
         " dar una descripcion clara de la actividad, para posteriormente seleccionar la fecha en la"
          " cual debe de ser entregada por los estudiantes."
        )
    st.write("")
    st.write("")
    st.markdown("<h6 style=' color: black; font-family: sans-serif;'> TAREA NUEVA </h6>", unsafe_allow_html=True)
    
    tarea = pd.DataFrame(
        { 
            'primera': [
                'Calculo',
                'Ingles',
                'Lengua',
                'Religion',
                'Electronica',
                'Ptp',
                'Fisica',
                'Gestion ambiental',
                'Educacion Fisica',
                'Quimica',
                'Direccion de curso',
                'Filosofia',
                'Artistica',
                'Tecnologia',
                'Catedra Fesanista',
                'Formacion Integral',
                'Investigacion',
                'Informatica'
            ],
        }
    )
    opcion = st.selectbox(
        'De que asignatura fue asignada la actividad:',
        tarea['primera'],
        key= "opci"
    )
    
    descripcion = st.text_input("Describe la actividad:", key="descrip")

    entrega = st.date_input("Fecha de entrega", value=None, key= "entr")

    boton = st.button("ENVIAR")
    anuncio_placeholder = st.empty()

    if boton and opcion and descripcion and entrega:
        fecha = entrega.strftime("%d/%m/%Y")
        # Cargar dase de datos de estudiantes
        base_datos = cargar_bd()

        # Modificación de lista tareas para cada estudiante en la base de datos
        for estudiante in base_datos:
            # diccionario de nuevas tareas
            nueva_tarea = {
                "asignatura": opcion,
                "descripcion": descripcion,
                "fecha": fecha,
                "estado": True
            }
            # agregar tarea a base de datos
            estudiante["lista_tareas"].append(
                nueva_tarea
            )

        actualizar_bd(base_datos)

        anuncio_placeholder.text(
                f"La actividad de {opcion} fue registrada con exito!, se entrega el {fecha}, los estudiantes deben: {descripcion}"
            )
        


#color
color = """
<style>
[data-testid="stAppViewContainer"] {
background-color: #44A19B;
}
</style>
"""

st.markdown(color, unsafe_allow_html= True)

def main():

    seleccion_pagina = {
    "iniciar sesion usuario": iniciar_estudiante,
     "iniciar sesion monitor": iniciar_monitor
    }

    seleccionador_pagina = st.sidebar.selectbox("seleccionar pagina", seleccion_pagina.keys())
    seleccion_pagina[seleccionador_pagina]()

if __name__ == "__main__":
    main()