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
        self.carros = []

    def adicionar_carro(self, carro):
        self.carros.append(carro)

    def listar_carros(self):
        if not self.carros:
            return "Nenhum carro na loja."
        return self.carros

    def encontrar_carros_por_modelo(self, modelo):
        carros_encontrados = [carro for carro in self.carros if carro.modelo.lower() == modelo.lower()]
        if not carros_encontrados:
            return []
        return carros_encontrados

    def remover_carro(self, modelo):
        carro_para_remover = None
        for carro in self.carros:
            if carro.modelo.lower() == modelo.lower():
                carro_para_remover = carro
                break
        if carro_para_remover:
            self.carros.remove(carro_para_remover)
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
            elif not ano.isdigit():
                st.error("O ano deve ser um número.")
            else:
                carro = Carro(marca, modelo, ano, imagem_url)
                loja.adicionar_carro(carro)
                st.success(f'{carro} foi adicionado.')

    elif escolha == "Listar todos os carros":
        st.subheader("Todos os carros na loja")
        carros = loja.listar_carros()
        if isinstance(carros, str):
            st.text(carros)
        else:
            for carro in carros:
                st.text(carro)
                if carro.imagem_url:
                    st.image(carro.imagem_url)

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

    elif escolha == "Remover um carro":
        st.subheader("Remover um carro")
        modelo = st.text_input("Digite o modelo do carro para remover")
        if st.button("Remover"):
            resultado = loja.remover_carro(modelo)
            st.success(resultado)

if __name__ == "__main__":
    main()
