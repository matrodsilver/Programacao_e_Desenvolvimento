from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)
DATABASE = 'sensores.db'


def criar_tabela():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS dados_sensores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sensor_id TEXT NOT NULL,
        temperatura REAL NOT NULL,
        umidade REAL NOT NULL
    )''')
    conn.commit()
    conn.close()


criar_tabela()


@app.route('/', methods=['POST', 'GET'])
def inserir_dados():
    if request.method == 'POST':
        dados = request.get_json()
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO dados_sensores (sensor_id, temperatura, umidade) VALUES (?, ?, ?)',
                    (dados['sensor_id'], dados['temperatura'], dados['umidade']))
        conn.commit()
        conn.close()
        return jsonify({"message": "Dados inseridos com sucesso"}), 201
    
    elif request.method == 'GET':
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM dados_sensores')
        rows = cursor.fetchall()
        conn.close()
        return jsonify(rows)


@app.route('/limpar-dados', methods=['DELETE'])
def limpar_dados():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM dados_sensores')
    conn.commit()
    conn.close()
    return jsonify({"message": "Dados limpos com sucesso"}), 200


if __name__ == '__main__':
    app.run(debug=True)
