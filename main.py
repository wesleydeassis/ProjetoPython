from os import write
import streamlit as st
from numpy.core.fromnumeric import size
import controllers.usuarioController as usuarioController
import models.usuario as usuario


with st.form(key="include_usuarios"):
    input_name = st.text_input(label="Insira o seu nome")
    input_email = st.text_input(label="Insira o seu email")
    input_departamento = st.selectbox("Selecione o departamento", [
                                      "Ti", "Financeiro", "comercial", "RH"])
    input_senha = st.text_input(label="Inseira sua senha")
    input_button_submit = st.form_submit_button("Enviar")

    if st.form_submit_button:
        usuario.nome = input_name
        usuario.email = input_email
        usuario.departamento = input_departamento
        usuario.senha = input_senha

        usuarioController.createUser(usuario)
