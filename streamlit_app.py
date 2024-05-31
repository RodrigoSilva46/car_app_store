import streamlit as st

class Carro:
    def __init__(self, marca, modelo, ano, cor, imagem_url=None):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.imagem_url = imagem_url

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.ano} {self.cor}'

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

    def remover_carros(self, indices):
        st.session_state['carros'] = [carro for i, carro in enumerate(st.session_state['carros']) if i not in indices]
        return f'Carros removidos com sucesso.'

def main():
    loja = LojaDeCarros()
    st.title("J Veículos")

    menu = ["Adicionar novo carro", "Listar todos os carros", "Buscar carros por modelo", "Remover carros"]
    escolha = st.sidebar.selectbox("Menu", menu)

    if escolha == "Adicionar novo carro":
        st.subheader("Adicionar novo carro")
        marca = st.text_input("Digite a marca do carro")
        modelo = st.text_input("Digite o modelo do carro")
        ano = st.text_input("Digite o ano do carro")
        cor = st.text_input("Digite a cor do carro")
        imagem_url = st.text_input("Digite a URL da imagem do carro (opcional)")

        if st.button("Adicionar Carro"):
            if not marca or not modelo or not ano or not cor:
                st.error("Todos os campos são obrigatórios.")
            elif not ano.isdigit():
                st.error("O ano deve ser um número.")
            else:
                carro = Carro(marca, modelo, ano, cor, imagem_url)
                loja.adicionar_carro(carro)
                st.success(f'{carro} foi adicionado.')

    elif escolha == "Listar todos os carros":
        st.subheader("Todos os carros na loja")
        carros = loja.listar_carros()
        if isinstance(carros, str):
            st.text(carros)
        else:
            indices_para_remover = []
            for i, carro in enumerate(carros):
                if st.checkbox(f'{carro}', key=f'carro_{i}'):
                    indices_para_remover.append(i)
                if carro.imagem_url:
                    st.image(carro.imagem_url)

            if indices_para_remover:
                if st.button("Remover carros selecionados"):
                    loja.remover_carros(indices_para_remover)
                    st.success("Carros removidos com sucesso.")
                    st.experimental_rerun()

    elif escolha == "Buscar carros por modelo":
        st.subheader("Buscar carros por modelo")
        modelo = st.text_input("Digite o modelo do carro para buscar")
        if st.button("Buscar"):
            carros = loja.encontrar_carros_por_modelo(modelo)
            if not carros:
                st.text(f'Nenhum carro encontrado com o modelo {modelo}.')
            else:
                for carro in carros:
                    st.text(carro)
                    if carro.imagem_url:
                        st.image(carro.imagem_url)

    elif escolha == "Remover carros":
        st.subheader("Remover carros")
        carros = loja.listar_carros()
        if isinstance(carros, str):
            st.text(carros)
        else:
            indices_para_remover = []
            for i, carro in enumerate(carros):
                if st.checkbox(f'{carro}', key=f'remover_{i}'):
                    indices_para_remover.append(i)
                if carro.imagem_url:
                    st.image(carro.imagem_url)

            if indices_para_remover:
                if st.button("Remover carros selecionados"):
                    loja.remover_carros(indices_para_remover)
                    st.success("Carros removidos com sucesso.")
                    st.experimental_rerun()

if __name__ == "__main__":
    main()
