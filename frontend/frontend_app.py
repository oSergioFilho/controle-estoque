import streamlit as st
import requests

# Coloque o IP do PC onde está rodando o Flask aqui!
API_URL = "http://localhost:5000"
# Exemplo se estiver em outra máquina: API_URL = "http://192.168.1.211:5000"

def listar_produtos():
    try:
        resp = requests.get(f"{API_URL}/produtos")
        if resp.status_code == 200:
            return resp.json()
        return []
    except Exception as e:
        st.error("Erro ao conectar no backend!")
        return []

def inserir_ou_alterar_produto(id, nome, quantidade):
    dados = {'nome': nome, 'quantidade': quantidade}
    if id:
        dados['id'] = id
    resp = requests.post(f"{API_URL}/produtos", json=dados)
    return resp.ok

def excluir_produto(id):
    resp = requests.delete(f"{API_URL}/produtos/" + str(id))
    return resp.ok

st.title("Controle de Estoque")

with st.form(key="produto_form"):
    id_edit = st.session_state.get('id_edit', None)
    nome = st.text_input("Nome", value=st.session_state.get('nome', ''))
    quantidade = st.number_input("Quantidade", min_value=0, value=st.session_state.get('quantidade', 0), step=1)
    submit = st.form_submit_button("Salvar")

    if submit:
        if nome.strip() == "":
            st.warning("Preencha o nome!")
        else:
            inserir_ou_alterar_produto(id_edit, nome, quantidade)
            st.success("Salvo com sucesso!")
            st.session_state['id_edit'] = None
            st.session_state['nome'] = ''
            st.session_state['quantidade'] = 0
            st.rerun()

st.subheader("Lista de Produtos")
produtos = listar_produtos()
for prod in produtos:
    col1, col2, col3, col4 = st.columns([1, 3, 2, 2])
    col1.write(prod['id'])
    col2.write(prod['nome'])
    col3.write(prod['quantidade'])
    editar = col4.button('Editar', key=f"edit_{prod['id']}")
    excluir = col4.button('Excluir', key=f"del_{prod['id']}")

    if editar:
        st.session_state['id_edit'] = prod['id']
        st.session_state['nome'] = prod['nome']
        st.session_state['quantidade'] = prod['quantidade']
        st.rerun()
    if excluir:
        excluir_produto(prod['id'])
        st.success("Excluído com sucesso!")
        st.rerun()
