# Proyecto_fesan

Primero se importa streamlit
```python
import streamlit as st
```
## Parte superior
En primera instancia en el codigo se crean 3 columnas 
```python
column1, column2 y column3
```
Esto para poner la imagen del logo en la parte superior izquierda de la pagina y en la parte superior al lado derecho del logo poder colocar el titulo, el cual se imprimio atraves de un markdown para poder ponerle decoracion o en otras palabras estilo.

## Inicio de sesion

En esta parte se dividio en dos partes la parte del inicio de sesion del estudiante y la parte del inicio de sesion del monitor.


```python
login.py
```


Para llevar a cabo ambos se creo el archivo login en el cual primero se encuentran las credenciales, las cuales son los usuarios y contraseñas de los usuarios.

```python
def authenticar (usuario, password):
```
Con esto en la autenticacion se verifica que el usuario coincida con la contraseña y si se cumple esta proposicion envia el valor de verdadero

```python
def login_page_usuario():
```
Posteriormente y en el mismo archivo login.py, se creo otra funcion la cual es la base del inicio de sesion del usuario donde se le pregunta el usuario y contraseña.

Si se cumplen las propocisiones de que el usuario oprima el boton y  halla colocado los valores verdadereas de authenticar; entonces arroja dos valores de estado de sesion y se recarga.

De la siguiente manera:

```python
if log and authenticar(usuario, password) :
        st.session_state["logged_in_usuario"] = True
        st.session_state["estudiante"] = usuario
        st.rerun()
```

Posteriormente sigue la parte del monitor:

primero se llama a la funcion authenticar:

```python
def authenticar_monitor (curso, password):
    if curso == "1101" and password == "Liceofesan11":
        return True
    return False
```
En esta funcion se verifica si el usuario y contraseña del monitor son los correctos; si es asi entonces se envia el valor de True y si no, se envia el valor de false.

```python
def login_page_monitor():
```

En esta funcion lo que se hace es crear la interfaz del inicio de sesion del monitor, en esta se coloca el titulo y se le pregunta al monitor, el usuario y contraseña; para posteriormente crear un condicional de si se cumple las proposiciones de log_monitor y authenticar_monitor:

```python
if log_monitor and authenticar_monitor(curso, password):
        st.session_state["logged_in_monitor"] = True
        st.rerun()
```
Si estas se cumplen entonces, el estado de sesion logged_in_monitor sera verdadero y se reiniciara el programa

```python
main.py
```
Volviendo al archivo main.py; ahora ya con las funciones login_page_usuario y login_page_monitor

lo primero que se hace es importar las funciones previamente mencionadas

```python
from login import login_page_usuario
from login import login_page_monitor
```

### Ya con esto se crean dos funciones:

#### Una para el usuario:

```python
def iniciar_estudiante():
    if "logged_in_usuario" not in st.session_state:
        st.session_state["logged_in_usuario"] = False
    
    if "estudiante" not in st.session_state:
        st.session_state["estudiante"] = ""

    if not st.session_state["logged_in_usuario"]:
        login_page_usuario()
    else:
        proyecto()
```
En esta se revisa si se cumple a cabalidad lo mencionado en el estado de sesion, si es asi se abre directamente la funcion proyecto y si no, entonces vuelve a aparecer login_page_usuario hasta que se cumpla lo del Session State.

#### La otra para el inicio de sesion del monitor:



```python
def iniciar_monitor():
    if "logged_in_monitor" not in st.session_state:
        st.session_state["logged_in_monitor"] = False

    if not st.session_state["logged_in_monitor"]:
        login_page_monitor()
    
    else:
        definir_tarea()
```
en este al igual que en el inicio de sesion del usuario se verifica si se cumple el session state, si es asi se abre la funcion definir_tarea y sino se abre login_page_monitor hasta que se cumpla lo del sesion state.

## Base de datos

Primero para poder llevar a cabo la funcion definir tarea y la funcion proyecto, se tuvo que crear dos funciones las cuales se encargan de cargar la base de datos y de actualizarla:


```python
def cargar_bd():
    bd = None
    with open("base_estudiantes.json", encoding="utf-8") as file:
        bd = json.load(file)
    return bd

def actualizar_bd(base_datos):
    with open("base_estudiantes.json", encoding="utf-8", mode="w") as file:
        json.dump(base_datos, file)
```

## Definir tarea

```python
def definir_tarea():
```
En primera instancia se imprime el titulo con un markdown y se muestra en texto una breve explicacion de como asignar una tarea.
```python
tarea = pd.DataFrame
```
se crea una lista con todas las asignaturas la cual se guarda en la variable tarea; y se crea un selectbox en el cual el usuario puede escoger un elemento de la lista.
```python
descripcion = st.text_input("Describe la actividad:", key="descrip")
```
se crea una variable descripcion en la cual se guarda la descripcion que da el monitor sobre la tarea.

```python
entrega = st.date_input("Fecha de entrega", value=None, key= "entr")
```
se crea una variable llamada entrega en donde se guarda  la fecha de entrega de la tarea

y por ultimo se crea un boton que envia la actividad.


se implementa un condicional en el cual si se cumple que:
- Se escoge asignatura en el selectbox
- Se escribe descripcion
- Se asigna fecha de entrega 
- Se pulsa en enviar 


```python
fecha = entrega.strftime("%d/%m/%Y")
```
se pasa el formato de date a str, para poder imprimirlo.
 ademas se carga la base de datos que se creo en el json en la funcion

```python
for estudiante in base_datos:
```
 se crea un condicional en el cual se le dice que a cada estudiante se crea una lista con una nueva tarea, la cual tiene:

 - nombre (asignatura)
 - descripcion(descripcion)
 - fecha(fecha)
 - estado de la tarea

luego con appened se adjunta la lista a la base de datos

```python
actualizar_bd(base_datos)
```
Se actualiza la base de datos

```python
f"La actividad de {opcion} fue registrada con exito!, se entrega el {fecha}, los estudiantes deben: {descripcion}"
```
Por ultimo se imprime con ayuda de un empty el texto anteriormente mencionado para que solamente cuando se cumpla la funcion este se muestre.

##  proyecto

Por otro lado y volviendo al inicio; cuando se cumple el session state en el inicio de sesion del usuario, se abre la funcion proyecto

```python
def proyecto():
```

Alli comienza por mostrarse el titulo a traves del mismo markdown usado en el titulo de la pagina; ademas se muestra una breve explicacion de como funciona el organizador de tareas.

```python
st1,st2,st3 = st.columns(3)
```
Ademas se crean tres columnas las cuales van a separar las tareas segun su prioridad:  la primera es prioridad alta, la segunda media y la tercera baja.

se crea una variable en la cual se almacena el estado de sesion del usuario
```python
estudiante = st.session_state["estudiante"]
    base_datos = cargar_bd()
```
si es True entonces significa que la tarea aun sigue activa y si es False, entonces la tarea ya no esta activa, ademas se carga en esta funcion la base de datos igual que en la funcion de definir_tarea.

luego se filtran los datos del estudiante actual y los datos de los demás estudiantes de la base de datos.


```python
with st.form(f"f{tarea}{tarea["fecha"]}"):
```
Para cada tarea activa, se crea un formulario con st.form, utilizando el identificador de la tarea y la fecha de la tarea como identificador único del formulario.


```python
fecha_presente = datetime.now()
fecha_tarea = datetime.strptime(tarea["fecha"], "%d/%m/%Y")
delta = fecha_tarea - fecha_presente
delta_dias = delta.days
```

se crea una variable con la fecha actual y otra con la fecha de la tarea en formato de datetime para luego restar las fechas y con ayda de la funcion .days lograr almacenar en una variable(delta_dias) la cantidad de dias que faltan para entregar esa tarea.

```python
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
```
Posteriormente se realizan unas condiciones segun la cantidad de dias que faltan para la entrega de la tarea: si faltan 3 o menos dias va a estar en la columna de prioridad alta, si faltan mas de 3 pero menos de 7, entonces se coloca en prioridad media y si faltan 7 dias o mas, entonces se coloca en la parte de prioridad baja.

Por ultimo
```python
if marcar:
    tarea["estado"] = False
    _datos_sin_estudiante.append(datos_estudiante)
    actualizar_bd(_datos_sin_estudiante)
    st.rerun()
```

 Se crea una condicion de que si se oprime sobre el boton de una de las tareas, entonces automaticamente el estado de esta tarea va a ser falso, por lo tanto se va a actualizar la base de datos y refrescar la pagina para que esta tarea ya no aparesca.

## Main

Se crea una funcion llamada main:

```python
def main():
```
Aqui se crea primero una lista, la cual esta compuesta por las funciones iniciar_estudiante r iniciar_monitor

se crea un slidebar, alli se pone una imagen del logo y un selectbox donde podra elegir dependiendo de su rol(usuario o monitor)
