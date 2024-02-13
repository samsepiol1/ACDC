import mysql.connector
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Configuração da conexão com o banco de dados MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'recomendacoes'
}

# Rota para atualizar uma recomendação
@app.route('/update_recommendation', methods=['POST'])
def update_recommendation():
    try:
        # Obtém os dados do POST
        data = request.json
        nome = data.get('nome')
        id_recomendacao = data.get('id')

        print(data)
        print(id_recomendacao)
        print(nome)

        # Faz uma requisição para o Deezer para buscar o link
        deezer_url = f"https://api.deezer.com/search?q={nome}"
        deezer_response = requests.get(deezer_url)

        # Verifica se a requisição ao Deezer foi bem-sucedida
        if deezer_response.status_code == 200:
            # Extrai os dados da resposta em formato JSON
            deezer_data = deezer_response.json()

            # Verifica se há dados retornados
            if 'data' in deezer_data and deezer_data['data']:
                # Extrai o primeiro item da lista de resultados
                primeiro_resultado = deezer_data['data'][0]

                # Obtém o link do primeiro resultado
                link_rec = primeiro_resultado.get('link')
                

                # Conecta ao banco de dados MySQL
                connection = mysql.connector.connect(**db_config)
               
                cursor = connection.cursor()

                # Atualiza o registro no banco de dados com o link encontrado
                update_query = "UPDATE recomendacoes SET reclink = %s WHERE id = %s"
                cursor.execute(update_query, (link_rec, id_recomendacao))
                
                connection.commit()

                # Fecha a conexão com o banco de dados
                cursor.close()
                connection.close()

                return jsonify({'message': f'Registro atualizado com sucesso. Novo link: {link_rec}'}), 200
            else:
                return jsonify({'message': 'Nenhum resultado encontrado no Deezer.'}), 404
        else:
            return jsonify({'message': 'Falha ao acessar a API do Deezer.'}), 500
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)