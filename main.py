from flask import Flask, jsonify, request
import pandas as pd

# cria uma instância da classe Flask e a associa ao nome do seu script ou módulo
app = Flask(__name__)

df_funcionarios = pd.read_excel("scr/BaseFuncionarios.xlsx")
dict_funcionarios = df_funcionarios.to_dict(orient='records')

@app.route('/funcionarios', methods=['GET'])
def get_funcionarios():
    return jsonify(dict_funcionarios)

def get_func_por_id(id):
    pass

app.run(port=5000, host='localhost', debug=True)