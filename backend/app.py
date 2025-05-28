from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

DB_PATH = os.path.join(os.path.dirname(__file__), "produtos.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT id, nome, quantidade FROM produtos')
    produtos = [{'id': row[0], 'nome': row[1], 'quantidade': row[2]} for row in c.fetchall()]
    conn.close()
    return jsonify(produtos)

@app.route('/produtos', methods=['POST'])
def inserir_ou_alterar():
    dados = request.get_json()
    nome = dados.get('nome')
    quantidade = dados.get('quantidade')
    id_produto = dados.get('id')
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    if id_produto:  # Alterar produto
        c.execute('UPDATE produtos SET nome = ?, quantidade = ? WHERE id = ?', (nome, quantidade, id_produto))
    else:  # Inserir novo produto
        c.execute('INSERT INTO produtos (nome, quantidade) VALUES (?, ?)', (nome, quantidade))
    conn.commit()
    conn.close()
    return jsonify({'status': 'ok'})

@app.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM produtos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    # O '0.0.0.0' garante que outros computadores na rede possam acessar
    app.run(host='0.0.0.0', port=5000)
