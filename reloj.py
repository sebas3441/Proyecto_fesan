import streamlit as st
import time


def display_temporizador():
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        remaining_time = 20 - elapsed_time
        if remaining_time <= 0:
            st.header("¡Tiempo Finalizado!")
            break
        mins, secs = divmod(remaining_time, 60)
        time_str = "{:02}:{:02}".format(int(mins), int(secs))
        st.header(time_str)
        time.sleep(0.5)
if st.button("Iniciar Temporizador"):
      display_temporizador()

