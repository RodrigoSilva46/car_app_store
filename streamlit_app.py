import streamlit as st

class Carro:
    def __init__(self, marca, modelo, ano, imagem_url=None):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.imagem_url = imagem_url

    def __str__(self):
        return f'{self.ano} {self.marca} {self.modelo}'

class LojaDeCarros:
    def __init__(self):
        if 'carros' not in st.session_state:
            st.session_state['carros'] = []

    def adicionar_carro(self, carro):
        st.session_state['carros'].append(carro)

    def listar_carros(self):
        if not st.session_state['carros']:
            return "Nenhum carro na loja."
        return st.session_state['carros']

    def encontrar_carros_por_modelo(self, modelo):
        carros_encontrados = [carro for carro in st.session_state['carros'] if carro.modelo.lower() == modelo.lower()]
        if not carros_encontrados:
            return []
        return carros_encontrados

    def remover_carro(self, modelo):
        carro_para_remover = None
        for carro in st.session_state['carros']:
            if carro.modelo.lower() == modelo.lower():
                carro_para_remover = carro
                break
        if carro_para_remover:
            st.session_state['carros'].remove(carro_para_remover)
            return f'{carro_para_remover} foi removido.'
        return f'Nenhum carro encontrado com o modelo {modelo}.'

def main():
    loja = LojaDeCarros()
    st.title("J Veículos")

    menu = ["Adicionar novo carro", "Listar todos os carros", "Buscar carros por modelo", "Remover um carro"]
    escolha = st.sidebar.selectbox("Menu", menu)

    if escolha == "Adicionar novo carro":
        st.subheader("Adicionar novo carro")
        marca = st.text_input("Digite a marca do carro")
        modelo = st.text_input("Digite o modelo do carro")
        ano = st.text_input("Digite o ano do carro")
        imagem_url = st.text_input("Digite a URL da imagem do carro (opcional)")

        if st.button("Adicionar Carro"):
            if not marca or not modelo or not ano:
                st.error("Todos os campos são obrigatórios.")
            elif not ano.isdigit
