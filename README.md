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


## Proyecto

Posteriormente cuando se cumple el session state en el inicio de sesion del usuario se abre la funcion proyecto

```python
def proyecto():
```

Alli comienza por mostrarse el titulo a traves del mismo markdown usado en el titulo de la pagina; ademas se muestra una breve explicacion de como funciona el organizador de tareas.

```python
st1,st2,st3 = st.columns(3)
```
Ademas se crean tres columnas las cuales van a separar las tareas segun su prioridad la primera es prioridad alta, la segunda media y la tercera baja.


#### La otra funcion es para el monitor:



### Inicio sesion usuario

```python
def my_function():
```

-
-
-
-

## Subtitulo
_te las escribe en cursiva_
**RESALTADAS**
~~DF~~

```python
def my_function():
```

-
-
-
-

## Subtitulo
_te las escribe en cursiva_
**RESALTADAS**
~~DF~~
