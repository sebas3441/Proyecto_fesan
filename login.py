import streamlit as st

CREDENTIALS = {
    "1234": "1234",
    "5678": "5678"
}

def authenticar (usuario, password):
    if usuario in CREDENTIALS.keys():
        if CREDENTIALS[usuario] == password:
            return True
    return False

def login_page_usuario():
    st.write("")
    st.write("")
    st.markdown("<h3 style='text-align: center; color: black; font-family: calibri; '>INICIO SESION USUARIO</h3>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    usuario = st.text_input("Usuario:")
    st.write("")
    password = st.text_input("Contraseña:", type="password")
    st.write("")
    c1, c2, c3 = st.columns(3)
    log = c2.button("**INICIAR SESION**")

    if log and authenticar(usuario, password) :
        st.session_state["logged_in_usuario"] = True
        st.session_state["estudiante"] = usuario
        st.rerun()


def authenticar_monitor (curso, password):
    if curso == "1101" and password == "Liceofesan11":
        return True
    return False

def login_page_monitor():
    st.write("")
    st.write("")
    st.markdown("<h3 style='text-align: center; color: black; font-family: calibri; '>INICIO SESION MONITOR</h3>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    curso = st.text_input("curso: ")
    st.write("")
    password = st.text_input("Contraseña: ", type= "password" )
    st.write("")
    c1, c2, c3 = st.columns(3)
    log_monitor = c2.button("**INICIAR SESION**")

    if log_monitor and authenticar_monitor(curso, password):
        st.session_state["logged_in_monitor"] = True
        st.rerun()
