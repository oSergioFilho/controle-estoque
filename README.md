Controle de Estoque - Projeto Fullstack com Flask e Streamlit

Descrição

Este projeto é um sistema simples de controle de estoque, desenvolvido como trabalho acadêmico. Ele demonstra um cenário de aplicação web fullstack com backend (API Flask + SQLite) e frontend (Streamlit) totalmente separados, além de poder ser integrado a um cenário de rede com NAT e firewall.

Estrutura do Projeto

controle-estoque/
├── backend/
│   └── app.py
├── frontend/
│   └── frontend_app.py
└── README.txt

Requisitos

- Python 3.x instalado (https://www.python.org/downloads/)
- Pacotes Python:
    - Flask
    - Flask-Cors
    - Streamlit
    - Requests

Instalação dos Pacotes

Execute os comandos abaixo no terminal/prompt de comando:

pip install flask flask-cors
pip install streamlit requests

Como Rodar

1. Backend (API Flask)

Abra o terminal, acesse a pasta backend e rode:

cd backend
python app.py

O backend irá rodar em http://localhost:5000 ou no IP da sua máquina (ex: http://192.168.1.211:5000/produtos).

2. Frontend (Streamlit)

Abra outro terminal, acesse a pasta frontend e rode:

cd frontend
streamlit run frontend_app.py

O Streamlit abrirá automaticamente o navegador (geralmente em http://localhost:8501/produtos).

Obs: Se o backend e frontend estiverem em máquinas diferentes, ajuste o API_URL em frontend_app.py para o IP do backend.

Funcionalidades

- Listar Produtos: Mostra todos os produtos cadastrados no estoque.
- Inserir Produto: Permite cadastrar novos produtos.
- Editar Produto: Permite editar um produto existente.
- Excluir Produto: Permite remover um produto do estoque.

Estrutura da API (Backend)

- GET /produtos
    - Lista todos os produtos cadastrados.

- POST /produtos
    - Insere ou edita produto (manda JSON com "nome", "quantidade" e opcionalmente "id").

- DELETE /produtos/<id>
    - Exclui o produto com o ID informado.

Exemplo de Uso da API

POST /produtos
Body (JSON):
{
  "nome": "Caneta",
  "quantidade": 20
}

Configuração de Rede (Firewall/NAT) - Resumo

- NAT Masquerade: Permite saída da rede interna para a internet.
- DNAT: Redireciona acessos externos para o backend Flask.
- Firewall: Só permite HTTP, HTTPS, DNS para internos e HTTP para externos.

Observações

- Projeto para fins didáticos.
- Se precisar de um vídeo demonstrativo ou mais informações de rede, veja o roteiro do professor ou pergunte ao responsável pelo projeto.

Autores

- Sergio jose de Almeida Filho
- Silvania Alves Oliveira
