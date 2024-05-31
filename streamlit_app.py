import streamlit as st
import sqlite3

# Função para criar a tabela de veículos
def criar_tabela():
    conn = sqlite3.connect("veiculos.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS veiculos (
        id INTEGER PRIMARY KEY,
        modelo TEXT,
        marca TEXT,
        ano INTEGER,
        cor TEXT,
        tipo TEXT,
        preco REAL,
        reservado INTEGER
    )
    """)
    conn.commit()
    conn.close()

# Função para adicionar um novo veículo
def adicionar_veiculo(modelo, marca, ano, cor, tipo, preco, reservado):
    conn = sqlite3.connect("veiculos.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO veiculos (modelo, marca, ano, cor, tipo, preco, reservado)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (modelo, marca, ano, cor, tipo, preco, reservado))
    conn.commit()
    conn.close()

# Função para listar os carros em estoque
def listar_carros():
    conn = sqlite3.connect("veiculos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM veiculos")
    carros = cursor.fetchall()
    conn.close()

    st.header("Carros em Estoque")
    if len(carros) > 0:
        st.write("Aqui estão os carros em estoque:")
        colunas = ["ID", "Modelo", "Marca", "Ano", "Cor", "Tipo", "Preço (R$)", "Reservado"]
        st.write(colunas)
        for carro in carros:
            st.write(carro)
    else:
        st.write("Não há carros em estoque.")

# Função para a página inicial do aplicativo
def home():
    st.title("Bem-vindo, Carolina!")
    st.sidebar.title("Opções")
    opcao = st.sidebar.radio("Escolha uma opção:", ["Adicionar Novo Veículo", "Carros em Estoque"])

    if opcao == "Adicionar Novo Veículo":
        st.header("Adicionar Novo Veículo")
        modelo = st.text_input("Modelo")
        marca = st.text_input("Marca")
        ano = st.number_input("Ano do Carro", min_value=1900, max_value=2024, step=1)
        cor = st.text_input("Cor")
        tipo = st.selectbox("Tipo", ["SUV", "Hatch", "Sedan"])
        preco = st.number_input("Preço (R$)", min_value=0.0, step=1.0)
        reservado = st.checkbox("Reservado")

        if st.button("Adicionar"):
            adicionar_veiculo(modelo, marca, ano, cor, tipo, preco, reservado)
            st.success("Veículo adicionado com sucesso!")

    elif opcao == "Carros em Estoque":
        listar_carros()

# Chamando a função para criar a tabela de veículos
criar_tabela()

# Chamando a função principal para executar o aplicativo
if __name__ == "__main__":
    home()

