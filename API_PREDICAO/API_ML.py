# Este script puxa o modelo armazenado numa maquina local e recebe as informações de um dataset para devolver a predição atraves do modelo armazenado criaando uma nova coluna para as predições

#################################

#      ATENÇÃO
# ESTE SCRIPT PARA FUNCIONAR, PRECISA ESTAR PREENCHIDO COM AS INFORMAÇOES DA MAQUINA, DOMINIO, E DO CAMINHO DO MODELO.

# SERÁ COMENTADO AO LADO DO CODIGO AS VARIAVEIS QUE PRECISAM SER PREENCHIDAS

#################################

from flask import Flask, request
import pickle
import pandas as pd

# Carregando modelo
caminhoModelo = "INSIRA O CAMINHO AQUI" # INFORMAR CAMINHO DO MODELO
model = pickle.load(open(caminhoModelo, 'rb'))

app = Flask( __name__)


#criando endpoint
@app.route('/predict', methods=['POST'])
def predict():
    test_json = request.get_json()

    # coletando os dados do dataframe que será predito
    if test_json:
        if isinstance(test_json, dict):
            df = pd.DataFrame(test_json, index=[0])
        
        else:
            df = pd.DataFrame(test_json, columns=test_json[0].keys())

    # Fazendo as predições e devolvendo pra API
    pred = model.predict(df)

    #Irá devolver para a API o dataframe informado com uma nova coluna contendo a predição
    df["prediction"] = pred
    response = df.to_json(orient='records')

    return response




if __name__ == '__main__':
    #pondo para o servidor local
    app.run(host='0.0.0.0', port='5000') 

